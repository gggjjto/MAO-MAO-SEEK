# MAO-MAO-SEEK   七天牛编程艺术节

1. 开发者信息 API

    - 获取开发者列表：返回所有注册的开发者信息，支持分页和基本的过滤（如按国家、领域）。
        - Endpoint: GET /developers
        - Query Parameters: country, field, page, limit

    - 获取单个开发者详细信息：返回指定开发者的详细信息，包括他们的 TalentRank、项目贡献、国家等。
        - Endpoint: GET /developers/{id}

2. 评级 API
    - 计算开发者 TalentRank：触发对单个开发者或所有开发者的 TalentRank 计算。
        - Endpoint: POST /rankings/compute
        - Body: { "developerId": "optional" } // 可选，如果未提供则为所有开发者计算

3. 项目 API
    - 获取项目列表：根据开发者的领域返回相关项目列表。
        - Endpoint: GET /projects
        - Query Parameters: field, page, limit
    - 获取单个项目详细信息：返回特定项目的详细信息，包括其星级、Forks、贡献者等。
        - Endpoint: GET /projects/{id}

4. 搜索 API
    - 搜索开发者：根据关键字（如姓名、技术栈、领域）搜索开发者。
        - Endpoint: GET /search/developers
        - Query Parameters: query, page, limit

5. 国家推测 API
    - 推测并更新开发者国家信息：基于开发者的网络和其他数据推测国家。
        - Endpoint: POST /developers/{id}/guess-nation

6. 用户认证与授权 API
    - 登录：用户登录以访问系统。
        - Endpoint: POST /auth/login
        - Body: { "username": "string", "password": "string" }
    - 注册：新用户注册。
        - Endpoint: POST /auth/register
        - Body: { "username": "string", "email": "string", "password": "string" }

```txt

	##### GitHub 数据应用
	
	根据 GitHub 的开源项目数据，开发一款开发者评估应用。
	
	基础功能（必须实现）
	
	1. 开发者在技术能力方面 TalentRank（类似 Google 搜索的 PageRank），对开发者的技术能力进行评价/评级。评价/评级依据至少包含：项目的重要程度、该开发者在该项目中的贡献度。
	2. 开发者的 Nation。有些开发者的 Profile 里面没有写明自己的所属国家/地区。在没有该信息时，可以通过其关系网络猜测其 Nation。
	3. 开发者的领域。可根据领域搜索匹配，并按 TalentRank 排序。Nation 作为可选的筛选项，比如只需要显示所有位于中国的开发者。
	
	高级功能（可选实现）
	
	1. 所有猜测的数据，应该有置信度。置信度低的数据在界面展示为 N/A 值。
	2. 开发者技术能力评估信息自动整理。有的开发者在 GitHub 上有博客链接，甚至有一些用 GitHub 搭建的网站，也有一些在 GitHub 本身有账号相关介绍。可基于类 ChatGPT 的应用整理出开发者评估信息。
	
	实现要求
	
	1. 与开发者能力评估相关部分功能实现，鼓励创新，其他技术方面允许使用现成的源代码或云服务，如数据采集框架、云计算、大模型服务等。

```

## 开发者信息 API

主要开发者的技术能力进行评价/评级

评价/评级的依据主要有：

- 参与项目的重要程度。
- 该开发者在该项目中的贡献度。
- 使用的语言和技术栈。
- 代码复杂性 - 使用静态代码分析工具来获取代码质量报告。
- 提交次数、创建的 PR 数量、报告和解决的问题数。
- 社区参与 - 用户的活动记录、提问和回答的次数、以及社区反馈（如 GitHub 上的星标、点赞等）

### GitHubSevice 类

```python
def __init__(self, access_token)  # 初始化GitHub客户端。


    def get_user(self, username)  # 根据用户名获取用户对象。


    def get_repositories(self, user)  # 获取用户的所有仓库。


    def get_organizations(self, user)  # 获取用户所属的组织。


    def get_contributions(self, user)  # 计算用户在所有仓库中的总提交次数。


    def get_repository_contributions(self, repo, username)  # 获取特定用户在指定仓库中的贡献比例。


    def get_contributed_repos_stars(self, username)  # 获取用户贡献的仓库及其星标数。


    def get_fetch_languages(self, username)  # 获取指定用户的所有仓库中使用的编程语言及其代码行数。


    def get_user_pull_requests(self, username)  # 获取用户创建的拉取请求总数。


    def get_user_issues(self, username)  # 获取用户创建的问题总数。


    def get_user_activity_stats(self, username)  # 获取用户的社区活动统计数据，包括提交次数、拉取请求、问题、接收的星标、分支和跟随者数。
```

