## 介绍

实现内容：提供 MOOC 课程链接，加载网页内容，构建知识库，大模型检索知识库进行回答。

## 演示

### MOOC 课程

![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052846851-25cd4ca2-730a-491d-a2d6-b26192e72e8d.png#averageHue=%23222a38&clientId=u27a99e96-c597-4&from=paste&height=586&id=u0cfd1852&originHeight=879&originWidth=1920&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=170565&status=done&style=none&taskId=u8344303c-b7e7-4b86-b9d1-3d9f664b055&title=&width=1280)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052861599-68ac46e8-e442-4ffa-a641-2f9b8dadc171.png#averageHue=%23242c39&clientId=u27a99e96-c597-4&from=paste&height=586&id=u1ab6b24f&originHeight=879&originWidth=1920&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=215131&status=done&style=none&taskId=ua4a4cd07-c6f3-403b-8253-d451e2aada1&title=&width=1280)![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052929381-c63b188b-771f-4d42-86d1-c394f4fd94fa.png#averageHue=%231f2735&clientId=u27a99e96-c597-4&from=paste&height=586&id=u27a6990d&originHeight=879&originWidth=1920&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=92838&status=done&style=none&taskId=uf61e44db-9651-4af4-8c15-292dfd5115a&title=&width=1280)

### 其他网页

![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707053077144-a5b7c4f2-7ff7-473d-b142-c5097bb3631c.png#averageHue=%23222a37&clientId=u27a99e96-c597-4&from=paste&height=586&id=uc178e487&originHeight=879&originWidth=1920&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=160531&status=done&style=none&taskId=uf7be4510-0276-4e03-87ba-9323420d7ec&title=&width=1280)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707053069742-c1a4a205-f177-4b2b-b19b-fca7d92f937f.png#averageHue=%23232b38&clientId=u27a99e96-c597-4&from=paste&height=586&id=u87932cc4&originHeight=879&originWidth=1920&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=195138&status=done&style=none&taskId=uc4747a10-fa90-4547-aad1-37ad171fe2d&title=&width=1280)

## 流程

![](https://cdn.nlark.com/yuque/0/2024/jpeg/2807993/1707050041200-73158594-1fe2-4d12-8d5f-a7b801d04acc.jpeg)<br />其中网址链接的提取先由模型进行提取尝试，若模型提取不出则再通过正则实现。

## DEBUG

### MOOC 课程

![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052696411-177798ee-31f5-4c93-8f07-6729e93b0102.png#averageHue=%2334302c&clientId=u27a99e96-c597-4&from=paste&height=556&id=uf69e88b2&originHeight=834&originWidth=1522&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=426321&status=done&style=none&taskId=u3d31e4b8-7faa-46f1-9fef-2f84540a289&title=&width=1014.6666666666666)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052712990-e69b18af-8c86-4937-baae-f84bf92f0171.png#averageHue=%23272625&clientId=u27a99e96-c597-4&from=paste&height=556&id=u2f3dc962&originHeight=834&originWidth=1522&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=184112&status=done&style=none&taskId=ud756e6bb-2793-479c-8293-cc5cfaa9eae&title=&width=1014.6666666666666)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707052829958-f42336a4-7e98-469a-93c2-c9bfd13433de.png#averageHue=%23272524&clientId=u27a99e96-c597-4&from=paste&height=556&id=u2b612b5b&originHeight=834&originWidth=1522&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=130643&status=done&style=none&taskId=u8840648a-c988-42d2-b31d-a7364903cac&title=&width=1014.6666666666666)

### 其他网页

![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707053032569-a1d733d1-62db-4ad2-ba58-8d40797982be.png#averageHue=%23292625&clientId=u27a99e96-c597-4&from=paste&height=556&id=ud64cca94&originHeight=834&originWidth=1522&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=215654&status=done&style=none&taskId=u93d16734-99cc-493a-82ed-4456373a84d&title=&width=1014.6666666666666)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1707053150336-96edc90f-9c26-4337-a2b0-418b2e55cdb3.png#averageHue=%23282624&clientId=u27a99e96-c597-4&from=paste&height=556&id=u10cc1cf6&originHeight=834&originWidth=1522&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=212525&status=done&style=none&taskId=ubb93047d-cd59-4661-9861-93dd5b6de25&title=&width=1014.6666666666666)

## 存在问题

1. 网页内容加载实际不全
2. 检索效果很一般
3. 模型输出会出现乱码情况
4. 向量数据库的存储块大小无法自我调整

## 未来可能拓展

> 时间原因没能实现

1. 模型微调（输出内容更标准化）
2. 量化部署（对比量化前后显存占用、模型表现）
3. 结合 Lagent 新增搜索功能
4. 对页面内容搭建图数据库（实体识别、关系抽取）
5. 用户提问对图数据库进行检索（三元组）

## 其他

[PyCharm远程运行调试代码](https://zhuanlan.zhihu.com/p/38591832)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/2807993/1706855337497-2b54983b-5bc2-40fd-9044-7d79b8bdcd07.png#averageHue=%232d2f33&clientId=u1eca6e11-e109-4&from=paste&height=672&id=brzNx&originHeight=1008&originWidth=1539&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=159735&status=done&style=none&taskId=u2675a299-f1bf-415d-bdbb-0c72955e7b5&title=&width=1026)