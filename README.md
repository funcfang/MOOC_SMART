## 介绍

实现内容：提供 MOOC 课程链接，加载网页内容，构建知识库，大模型检索知识库进行回答。

## 配置

语言模型：Shanghai_AI_Laboratory/internlm-chat-7b

向量模型：sentence-transformer

框架：LangChain

演示：Gradio

## 演示

### MOOC 课程

![img](README.assets/20240204215359-71.png)

![img](README.assets/20240204215419-72.png)

![img](README.assets/1707052929381-c63b188b-771f-4d42-86d1-c394f4fd94fa-17070549115608.png)

### 其他网页

![img](README.assets/20240204215454-6f.png)

![img](README.assets/1707053069742-c1a4a205-f177-4b2b-b19b-fca7d92f937f.png)

## 流程

![img](README.assets/1707053069742-c1a4a205-f177-4b2b-b19b-fca7d92f937f-170705493508611.png)

其中网址链接的提取先由模型进行提取尝试，若模型提取不出则再通过正则实现。

## DEBUG

### MOOC 课程

![img](README.assets/1707052696411-177798ee-31f5-4c93-8f07-6729e93b0102.png)

![img](README.assets/1707052712990-e69b18af-8c86-4937-baae-f84bf92f0171.png)

![img](README.assets/1707052829958-f42336a4-7e98-469a-93c2-c9bfd13433de.png)

### 其他网页

![img](README.assets/1707053032569-a1d733d1-62db-4ad2-ba58-8d40797982be.png)

![img](README.assets/1707053150336-96edc90f-9c26-4337-a2b0-418b2e55cdb3.png)

## 存在问题

> 时间原因没能解决

1. 网页内容加载实际不全
2. 检索效果很一般
3. 模型输出会出现乱码情况
4. 向量数据库的存储文本分块没调好

## 未来可能拓展

> 时间原因没能实现

1. 模型微调（输出内容更标准化）
2. 量化部署（对比量化前后显存占用、模型表现）
3. 结合 Lagent 新增搜索功能
4. 对页面内容搭建图数据库（实体识别、关系抽取）
5. 用户提问对图数据库进行检索（三元组）

## 其他

[PyCharm远程运行调试代码](https://zhuanlan.zhihu.com/p/38591832)

![img](README.assets/1706855337497-2b54983b-5bc2-40fd-9044-7d79b8bdcd07.png)