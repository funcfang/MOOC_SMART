import gradio as gr
from LLM import InternLM_LLM
from util import load_chain, init_database, init_download_model
import langchain
langchain.debug = True
default_value = [(None, '您好！我能根据你提供的MOOC课程链接进行问答，输入你想了解的MOOC网址链接给我吧，我会尽可能帮你解答~\
      \n您可以像这样输入：我想了解的MOOC链接是：https://www.icourse163.org/course/ZJU-1003377027')]


class Model_center:
    """
    存储检索问答链的对象
    """
    init_download_model()

    def __init__(self):
        # 构造模型
        self.llm = InternLM_LLM(model_path="Shanghai_AI_Laboratory/internlm-chat-7b")
        self.vectordb = None
        self.chain = None

    def load_chain(self, vectordb):
        # 构造函数，加载检索问答链
        self.vectordb = vectordb
        self.chain = load_chain(self.llm, vectordb)

    def reset(self):
        self.chain = None
        self.vectordb.delete_collection()
        return "", default_value

    def qa_chain_self_answer(self, question: str, chat_history: list = []):
        """
        调用问答链进行回答
        """
        if question is None or len(question) < 1:
            return "", chat_history
        try:

            if self.chain is None:
                # 对提问中存在的网址构建知识库
                result_url, page_title, vectordb = init_database(user_input_with_url=question, llm=self.llm)
                if vectordb is None:
                    answer = f"您的提问中好像不存在网址链接或者网址链接有错误，请重新试试输入你要发起提问的网址链接~"
                else:
                    self.load_chain(vectordb)
                    answer = f"您想要了解的网址链接为: {result_url}，页面标题为: {page_title}, 我已经初始化该页面知识库完成！欢迎来向我提问吧~"

            else:
                answer = self.chain({"query": question})['result']

            # 将问答结果直接附加到问答历史中，Gradio 会将其展示出来
            chat_history.append((question, answer))
            return '', chat_history
        except Exception as e:
            return e, chat_history


# 实例化核心功能对象
model_center = Model_center()
# 创建一个 Web 界面
block = gr.Blocks()
with block as demo:
    with gr.Row(equal_height=True):
        with gr.Column(scale=15):
            # 展示的页面标题
            gr.Markdown("""<h1><center>MOOC课程链接问答</center></h1>
                <center>其实只要是个网页就行</center>
                """)

    with gr.Row():
        with gr.Column(scale=4):
            # 创建一个聊天机器人对象
            chatbot = gr.Chatbot(height=450, show_copy_button=True, value=default_value)
            # 创建一个文本框组件，用于输入 prompt。
            msg = gr.Textbox(label="Prompt/问题")

            with gr.Row():
                # 创建提交按钮。
                db_wo_his_btn = gr.Button("聊天")
            with gr.Row():
                # 创建一个清除按钮，用于清除聊天机器人组件的内容。
                clear_btn = gr.Button("重新对新的MOOC课程链接发起提问")

        # 设置按钮的点击事件。当点击时，调用上面定义的 qa_chain_self_answer 函数，并传入用户的消息和聊天历史记录，然后更新文本框和聊天机器人组件。
        db_wo_his_btn.click(model_center.qa_chain_self_answer, inputs=[
            msg, chatbot], outputs=[msg, chatbot])
        clear_btn.click(model_center.reset, outputs=[msg, chatbot])

    gr.Markdown("""提醒：<br>
    1. 初始化网站知识库时间可能较长，请耐心等待。
    2. 使用中如果出现异常，将会在文本输入框进行展示，请不要惊慌。
    3. 可参考使用的部分课程链接：https://www.icourse163.org/course/ZJU-1003377027、https://www.icourse163.org/course/NUDT-1466045161、https://www.icourse163.org/course/PKU-1002188003
    <br>
    """)
gr.close_all()
# 直接启动
demo.launch()
