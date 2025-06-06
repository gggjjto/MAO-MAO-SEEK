## MAO-MAO-SEEK

<img src="./docs/picture/logo.png" alt="logo" style="zoom:25%;" />

### 应用介绍

MAO-MAO-SEEK 是一款基于 GitHub 开源项目数据的开发者评估应用，旨在帮助企业、技术社区、以及个人更好地理解和衡量开发者的技术能力与影响力。通过对开源贡献和开发者社交网络的深度分析，TalentRank
评估开发者的技术能力，揭示其在全球开发者生态中的地位。应用将多维度地展示开发者的影响力、领域专长及其地域分布，帮助用人单位寻找合适的开发者，也为开发者提供展示自身能力的透明渠道。

### 项目地址

[MAO-MAO-SEEK](https://github.com/gggjjto/MAO-MAO-SEEK)

~~~shell
git clone https://github.com/gggjjto/MAO-MAO-SEEK.git
~~~

### 核心功能

1. **开发者查询与评估**： 用户可以通过输入开发者的 GitHub
   用户名，获取关于该开发者的详细信息，包括其所在国家（如有明确标明）、粉丝数量、关注数量、参与的仓库数量，以及其技术能力评分（TalentRank）。该评分基于开发者在开源项目中的贡献和影响力，以量化的方式展示开发者在整个社区中的地位。

2. **开发者排行榜**：
   应用提供了全球以及区域性的开发者排行榜，用户可以按国家、地区、或领域来筛选开发者，并按照技术评分从高到低进行排序。这使得企业和团队能够快速找到符合条件的顶尖开发者，也方便开发者了解自身的社区排名和影响力。

3. **数据可信度标识**：
   针对从社交网络推测得出的开发者信息，应用引入了数据置信度概念。如果某些数据（如位置）是基于推测得出的，那么会为该信息提供置信度标识。置信度较低的部分会被标记为 `N/A`
   ，帮助用户更好地理解这些数据的可靠性。

4. **交互式可视化界面**： 我们为开发者评估提供了友好的交互界面，开发者在个人页面中可以看到自己过去一年的活跃情况（类似于
   GitHub 提交的绿点图），以及个人简介的汇总信息，这些数据为开发者的能力评估提供了丰富的参考。

### 项目愿景

MAO-MAO 诞生于 1024 创造节，对热爱开源编程的开发者们的一次有趣的数据分析尝试。希望通过这款应用，能够让开发者社区变得更加透明和可衡量，帮助那些默默为开源项目贡献的人们获得更多的认可。

### 项目启动

接下来我将介绍前端和后端的启动

##### 前端

前端使用的是 TypeScript + Vue+Vuetify 。在这里我们提供前端的启动方式，打开项目中 MAO-MAO-SEEK-UI 文件夹

```shell
cd MAO-MAO
npm install
npm run dev
```

##### 后端

后端使用的是 Python + Flask 。

首先需要在项目的根目录下创建一个 config.py
文件，将申请的阿里百炼大模型的 [API Key](https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key?spm=a2c4g.11186623.0.0.331f453aaoLGmI)
写入

```python
DASHSCOPE_API_KEY = ""
```

下面是后端的环境配置，项目使用的是 Python 3.11

```shell
# 先要启动 Redis 哦！
pip install -r requirements.txt
# 在根目录下的 app.py 中进行启动即可
# 记得自己创建配置文件哦!
```

### 架构设计

![框架设计](./docs/picture/%E6%A1%86%E6%9E%B6%E5%9B%BE.png)

### 模块设计

![模块设计](./docs/picture/%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1.png)

### 联系作者

- 程序由我个人独立开发， 能力有限，难免出现一些Bug，欢迎大家积极反馈Bug和提出优化建议。

- 个人邮箱：1471104705qq.com

### maomaoseek 重置计划
参加比赛时，时间短，任务重，很多功能没有实现，现在出来工作了，有时间完善一下项目，
重置计划如下：
      - 重构代码框架，使用Fastapi + postgreSQL + Redis。
      - 添加Github登录的功能。

