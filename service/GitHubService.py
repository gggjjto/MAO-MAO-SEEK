import time

from github import Github

import config
from common.FromCountry import guess_nation, extract_country_one
from common.GQL.GQLQueryGitHub import *
from common.GraphQLConfig import GraphQLConfig
from common.SendMessage import get_repository_languages


class GitHubService:

    def __init__(self):
        """
        初始化GitHub客户端。
        """
        self.client = GraphQLConfig(config.GITHUB_ACCESS_TOKEN)
        self.user = Github(config.GITHUB_ACCESS_TOKEN)

    def get_user_info(self):
        """
        根据用户名获取用户信息。
        :return: 用户对象。
        """
        user = self.user.get_user()
        return {
            'login': user.login,
            'name': user.name,
            'public_repos': user.public_repos,
            'followers': user.followers,
            'following': user.following,
            'location': user.location
        }

    def get_user(self, username):
        """
        根据用户名获取用户对象。
        :param username: GitHub用户名。
        :return: 用户对象。
        """
        result = self.client.github_graphql(user_query, username)
        if 'data' in result and 'user' in result['data']:
            user = result['data']['user']
            return {
                'login': user.get('login', ''),
                'name': user.get('name', ''),
                'public_repos': user['repositories']['totalCount'],
                'followers': user['followers']['totalCount'],
                'following': user['following']['totalCount'],
                'location': user.get('location', None)
            }
        else:
            return None

    def get_user_location(self):
        """
        获取用户位置信息。
        :return: 用户位置信息和N/A值。
        """
        user = self.user.get_user()
        location = user.location
        max_country = ""
        reliability = 1
        if location is None:
            max_country, reliability = guess_nation(user.login)
        else:
            max_country = extract_country_one(location)
            max_country = max_country.decode('utf-8')
        return max_country, reliability

    def get_location(self, username):
        """
        根据用户名获取用户位置信息。
        :param username: GitHub用户名。
        :return: 用户对象。
        """
        user = self.user.get_user(username)
        location = user.location
        max_country = ""
        reliability = 1
        if location is None:
            max_country, reliability = guess_nation(user.login)
        else:
            max_country = extract_country_one(location)
            max_country = max_country.decode('utf-8')
        return max_country, reliability

    def get_repositories(self, username):
        """
        获取用户的所有仓库。
        :param username: 用户对象。
        :return: 用户的仓库列表。
        """
        result = self.client.github_graphql(get_repositories_query, username)
        if 'data' in result and 'user' in result['data'] and 'repositories' in result['data']['user']:
            return [
                {
                    'name': repo['name'],
                    'is_private': repo['isPrivate'],
                    'stars': repo['stargazerCount'],
                    'forks': repo['forkCount'],
                    'description': repo.get('description', ''),
                    'watch': repo['watchers']['totalCount']
                }
                for repo in result['data']['user']['repositories']['nodes']
            ]
        else:
            return []

    def get_organizations(self, username):
        """
        获取用户所属的组织。
        :param username: 用户对象。
        :return: 组织列表。
        """
        result = self.client.github_graphql(get_organizations_query, username)
        if 'data' in result and 'user' in result['data'] and 'organizations' in result['data']['user']:
            return [
                {
                    'name': org['name'],
                    'url': org['url'],
                    'description': org.get('description', None)
                }
                for org in result['data']['user']['organizations']['nodes']
            ]
        else:
            return []

    def get_contributions(self, username):
        """
        计算用户一年的贡献。
        :param username: 用户对象。
        :return: 总提交次数。
        """
        data = self.client.github_graphql(get_contributions_query, username)
        total_contributions = (
            data)['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
        return total_contributions

    def get_repository_contributions(self, repo, username, owner):
        """
        获取特定用户在指定仓库中的贡献比例。
        :param repo: 仓库名。
        :param username: 用户名。
        :param owner: 仓库所有者
        :return: 用户的贡献比例。
        """
        data = self.client.send_query(get_repository_contributions_query, {"owner": owner, "repoName": repo})
        # 计算用户贡献比例
        if 'data' in data and 'repository' in data['data']:
            total_contributions = 0
            user_contributions = 0
            edges = data['data']['repository']['defaultBranchRef']['target']['history']['edges']
            for edge in edges:
                if edge['node']['author']['user']:
                    if edge['node']['author']['user']['login'].lower() == username.lower():
                        user_contributions += 1
                    total_contributions += 1

            if total_contributions > 0:
                contribution_percentage = (user_contributions / total_contributions) * 100
                return contribution_percentage
        return 0

    def get_contributed_repos_stars(self, username):
        """
        获取用户贡献的仓库及其星标数。
        :param username: 用户名。
        :return: 列表，包含仓库名、星标数、是否分支、仓库拥有者、仓库url。
        """
        repos = []
        result = self.client.github_graphql(get_contributed_query, username)
        if result and 'data' in result and 'user' in result['data']:
            for repo_node in result['data']['user']['repositories']['nodes']:
                repo_name = repo_node['name']
                stargazers_count = repo_node['stargazers']['totalCount']
                url = repo_node['url']
                is_fork = repo_node['isFork']
                owner = repo_node['owner']['login']
                repos.append({
                    'repo_name': repo_name,
                    'stars': stargazers_count,
                    'isFork': is_fork,
                    'owner': owner,
                    'url': url
                })
        return repos

    def get_user_repos_contributions(self, username):
        """
        获取用户贡献的仓库的分数
        :param username: 用户名。
        :return: 用户贡献的仓库的分数
        """
        repos = self.get_contributed_repos_stars(username)
        repos_score = 0
        for repo in repos:
            contribution_percentage = self.get_repository_contributions(repo['repo_name'], username, repo['owner'])
            repos_score += contribution_percentage * repo['stars']
        return repos_score

    def get_user_score(self, username):
        user = self.get_user(username)
        followers = user['followers']
        repos_score = self.get_user_repos_contributions(username)
        score = repos_score + followers
        return score


    def get_fetch_languages(self, username):
        """
        获取指定用户的所有仓库中使用的编程语言及其代码行数。
        :param username: GitHub 用户名
        :return: 一个字典对象，包含语言及其对应的字节
        """

        data = self.get_contributed_repos_stars(username)
        result = {}
        for res in data:
            if not res['isFork']:
                mp = get_repository_languages(res['owner'], res['repo_name'])
                result.update(mp)

        return result

    def get_user_pull_requests(self, username):
        """
        获取用户创建的拉取请求总数。
        :param username: 用户名。
        :return: 返回用户创建的所有仓库的拉取请求总数。
        """
        result = self.client.github_graphql(get_user_pull_requests_query, username)
        total_prs = 0

        if result and 'data' in result and 'user' in result['data'] and 'pullRequests' in result['data']['user']:
            total_prs = result['data']['user']['pullRequests']['totalCount']

        return total_prs

    def get_user_issues(self, username):
        """
        获取用户创建的问题总数。
        :param username: 用户名。
        :return: 返回用户在其所有仓库中报告的问题总数。
        """
        result = self.client.github_graphql(get_user_issues_query, username)
        total_issues = 0

        if result and 'data' in result and 'user' in result['data'] and 'issues' in result['data']['user']:
            total_issues = result['data']['user']['issues']['totalCount']

        return total_issues

    def get_user_activity_stats(self, username):
        """
        获取用户的社区活动统计数据，包括提交次数、拉取请求、问题、接收的星标、分支和跟随者数。
        :param username: 用户名。
        :return: 包含各种社区活动统计的字典。
        """
        result = self.client.github_graphql(get_user_activity_stats_query, username)

        if result and 'data' in result and 'user' in result['data']:
            user_data = result['data']['user']
            total_stars_received = sum(repo['stargazers']['totalCount'] for repo in user_data['repositories']['nodes'])
            total_forks_received = sum(repo['forkCount'] for repo in user_data['repositories']['nodes'])
            return {
                'total_commits': user_data['contributionsCollection']['totalCommitContributions'],
                'total_pull_requests': user_data['pullRequests']['totalCount'],
                'total_issues': user_data['issues']['totalCount'],
                'total_stars_received': total_stars_received,
                'total_forks_received': total_forks_received,
                'followers_count': user_data['followers']['totalCount']
            }
        return {}


def get_rate_limit(token):
    g = Github(token)
    now = time.time()
    ratelimit = g.rate_limiting
    remaining = ratelimit[0]
    reset_time = g.rate_limiting_resettime
    minutes_left = (reset_time - now) / 60
    if remaining == 0:
        print(minutes_left)
    return remaining
