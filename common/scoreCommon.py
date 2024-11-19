from flask import session

import config
from common.GraphQLConfigCommon import GraphQLConfig
from common.SendMessageCommon import send_response
from common.Tool.MultiThreadHelperCommon import MultiThreadHelper
from common.Tool.RedisCommon import RedisTool

query_followers = """
query ($login: String!) {
  user(login: $login) {
    followers {
      totalCount
    }
  }
}
"""
query_repos = """
query ($login: String!, $after: String) {
  user(login: $login) {
    repositories(first: 100, privacy: PUBLIC, after: $after) {
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        name
        description
        url
        stargazerCount
        forkCount
        createdAt
      }
    }
  }
}
"""

query_contributors = """
query ($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    mentionableUsers(first: 50, after: $after) {
      nodes {
        login
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
"""


def get_repos(gql, login):
    # 查询用户仓库
    # 设置初始参数
    variables = {
        "login": login,  # 替换为您要查询的用户名
        "after": None  # 初始时为 None，表示从第一个仓库开始
    }
    # 发送请求以分页获取所有仓库
    all_repositories = []

    while True:
        try:
            data = gql.send_query(query_repos, variables)
            repositories = data['data']['user']['repositories']['nodes']
            all_repositories.extend(repositories)
            # 检查是否有下一页
            page_info = data['data']['user']['repositories']['pageInfo']
            if page_info['hasNextPage']:
                # 更新 endCursor，获取下一页
                variables['after'] = page_info['endCursor']
            else:
                # 没有下一页，跳出循环
                break
        except Exception as e:
            print("在get_repos函数中查询开发者repos失败，错误是: {e}")
            return None

    return all_repositories


def get_contributors(repo_url, login):
    # 查询用户对仓库的贡献
    owner, repo = repo_url.split("/")[-2:]
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"  # GitHub API 端点
    headers = {
        "Authorization": f"Bearer {config.GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "per_page": 50,
        "page": 1
    }
    x = 80  # 不在前50名
    try:
        contributors = send_response(url, headers, params)
        if contributors == 403:
            return 30
        elif contributors == 204:
            return -1
        for index, contributor in enumerate(contributors, start=1):
            print(f"Rank #{index}: {contributor['login']} - Contributions: {contributor['contributions']}")
            if contributor['login'] == login:
                return index
    except Exception as e:
        print(f"在get_contributors函数中查询开发者contributors失败，错误是: {e}")
        return -1

    return x


def get_sum(repo_url, stars, login):
    index = get_contributors(repo_url, login)
    if index == -1:
        return 0
    if (81 - index) >= 50:
        num = 81 - index
    else:
        num = 30
    num = num / 100
    o = stars * num
    return o


redis = RedisTool(db=1)


def get_user_score(login):
    score = redis.get_value(login)
    if score is None:
        score = get_score(login)
        redis.set_value(login, score)
    print(f'login:{login} - score = {score}')
    return score


def get_score(login):
    """
    对开发者的技术能力进行评分
    :param login: 用户名
    :return:
    """
    token = session['token']
    # token = config.GITHUB_ACCESS_TOKEN
    gql = GraphQLConfig(token)
    # 1.获取开发者的 followers
    try:
        followers_data = gql.send_query(query_followers, {"login": login})
        followers_count = followers_data['data']['user']["followers"]["totalCount"]
        print(f"开发者：{login} 的followers数量是：{followers_count}")
    except Exception as e:
        print(f"在get_score函数中查询开发者followers失败，错误是: {e}")
        return 0

    # 2.获取开发者公开仓库。
    all_repositories = get_repos(gql, login)
    multi_thread_helper = MultiThreadHelper(max_workers=20)
    futures = []
    for repo in all_repositories:
        print(f"Name: {repo['name']}, Stars: {repo['stargazerCount']}, URL: {repo['url']}")
        repo_url = repo["url"]
        stars = repo["stargazerCount"]
        # 3.获取仓库的star，contributors信息，计算开发者贡献率，按照参加的排名进行百分比计算，第一名的百分比为80%，第二名的百分比是79%，以此类推到50名，第50名及其以后的名次都按照百分比是30%的计算
        futures.append(multi_thread_helper.submit_task(get_sum, repo_url, stars, login))
    # 4.按照 followers + all(star * con%)计算评分
    results = multi_thread_helper.wait_for_all(futures)
    sum = 0
    for result in results:
        sum += result
    multi_thread_helper.shutdown()
    score = followers_count + sum
    print(f"开发者: {login} 最后的得分是：{score}")
    return score


# 示例使用
if __name__ == "__main__":
    login = "torvalds"
    score = get_score(login)
