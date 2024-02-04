import re

from LLM import InternLM_LLM
from langchain.vectorstores import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


def is_valid_website(url):
    # 检查字符串是否以"http://"、"https://"、或"www."开头，并且包含"."字符
    if url.startswith("http://") or url.startswith("https://") or url.startswith("www."):
        if "." in url:
            return True

    return False


def extract_urls(text):
    # 修正的正则表达式，允许链接结尾是数字
    url_pattern = re.compile(r'https?://\S+|www\.\S+|\S+\.\d+')

    # 使用正则表达式查找所有匹配的链接
    urls = re.findall(url_pattern, text)

    return urls


from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os


def init_download_model():
    model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b'
                                  , cache_dir='./', revision='v1.0.3')
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    # 下载模型
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir sentence-transformer')


def init_database(user_input_with_url, llm=None):
    # 加载模型
    if llm is None:
        llm = InternLM_LLM(model_path="Shanghai_AI_Laboratory/internlm-chat-7b")
    query = f"""
    要求:提取用户输入内容中的网址链接
    以下为用户的输入内容：
    '''
    {user_input_with_url}
    '''
    根据以上用户输入内容，若存在网址链接则直接输出相应的链接，不存在则输出'不存在'。
    你的输出:
    """
    url_result = llm.predict(query)
    url_ = extract_urls(query)
    if url_result == '不存在' or not is_valid_website(url_result):
        print('error output url: ', url_result)
        if len(url_) == 0:
            return url_result, '', None
        url_result = url_[0]
    # 加载目标网页
    try:
        loader = WebBaseLoader(url_result)
        doc = loader.load()
    except Exception as e:
        print('error load url: ', url_result)
        return url_result, '', None
    # 使用replace方法将多个连续的换行符替换为一个
    doc[0].page_content = re.sub('\n+', '\n', doc[0].page_content)
    page_title = doc[0].metadata['title'].replace("\n", "")
    # 对文本进行分块
    text_splitter = CharacterTextSplitter(
        separator="  ",
        chunk_size=100,
        chunk_overlap=50,
        length_function=len,
    )
    split_docs = text_splitter.split_documents(doc)

    # 加载开源词向量模型
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformer")

    # 构建向量数据库
    # 定义持久化路径
    persist_directory = 'data_base/vector_db/chroma'
    # 加载数据库
    vectordb = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        # persist_directory=persist_directory  # 允许我们将persist_directory目录保存到磁盘上
    )
    # 将加载的向量数据库持久化到磁盘上
    # vectordb.persist()
    return url_result, page_title, vectordb


def load_chain(llm, vectordb):
    # 加载问答链

    # 我们所构造的 Prompt 模板
    template = """
    根据以下内容信息来回答问题，我相信你是很聪明的，你是能够从以下内容中分析出答案的。但如果你真不知道答案，就回答'对不起，知识库内容有限，我不知道。试试换个问题问我吧~'。”
    内容信息：
    '''
    {context}
    '''
    问题: {question}
    你的回答:
    """

    # 调用 LangChain 的方法来实例化一个 Template 对象，该对象包含了 context 和 question 两个变量，在实际调用时，这两个变量会被检索到的文档片段和用户提问填充
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever(), return_source_documents=True,
                                           chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    return qa_chain
