from collections import Counter

from github import Github

import config


class GitHubService:

    def __init__(self):
        """
        初始化GitHub客户端。
        :param access_token: 用于GitHub API认证的访问令牌。
        """
        access_token = config.GITHUB_ACCESS_TOKEN
        self.client = Github(access_token)

    def get_user(self, username):
        """
        根据用户名获取用户对象。
        :param username: GitHub用户名。
        :return: 用户对象。
        """
        return self.client.get_user(username)

    @staticmethod
    def get_repositories(user):
        """
        获取用户的所有仓库。
        :param user: 用户对象。
        :return: 用户的仓库列表。
        """
        return user.get_repos()

    @staticmethod
    def get_organizations(user):
        """
        获取用户所属的组织。
        :param user: 用户对象。
        :return: 组织列表。
        """
        return user.get_orgs()

    @staticmethod
    def get_contributions(user):
        """
        计算用户在所有仓库中的总提交次数。
        :param user: 用户对象。
        :return: 总提交次数。
        """
        total_commits = 0
        for repo in user.get_repos():
            stats = repo.get_stats_contributors()
            if stats:
                for stat in stats:
                    if stat.author.login.lower() == user.login.lower():
                        total_commits += stat.total
        return total_commits

    @staticmethod
    def get_repository_contributions(repo, username):
        """
        获取特定用户在指定仓库中的贡献比例。
        :param repo: 仓库对象。
        :param username: 用户名。
        :return: 用户的贡献比例。
        """
        contributors = repo.get_contributors()
        total_contributions = 0
        user_contributions = 0
        for contributor in contributors:
            contributions = contributor.contributions
            total_contributions += contributions
            if contributor.login.lower() == username.lower():
                user_contributions = contributions

        if total_contributions == 0:
            return 0
        return user_contributions / total_contributions

    def get_contributed_repos_stars(self, username):
        """
        获取用户贡献的仓库及其星标数。
        :param username: 用户名。
        :return: 列表，包含仓库名、星标数和用户贡献比例。
        """
        user = self.get_user(username)
        repos = []
        for repo in user.get_repos():
            if repo.fork:
                parent = repo.parent
                contribution_scale = self.get_repository_contributions(parent, user.login)
                repos.append([repo.name, parent.stargazers_count, contribution_scale])
            else:
                repos.append([repo.name, repo.stargazers_count, 1])
        return repos

    def get_fetch_languages(self, username):
        """
        获取指定用户的所有仓库中使用的编程语言及其代码行数。
        :param username: GitHub 用户名
        :return: 一个Counter对象，包含语言及其对应的代码行数
        """
        user = self.get_user(username)
        language_stats = Counter()

        for repo in user.get_repos():
            languages = repo.get_languages()
            for language, lines in languages.items():
                language_stats[language] += lines

        return language_stats

    def get_user_pull_requests(self, username):
        """
        获取用户创建的拉取请求总数。
        :param username: 用户名。
        :return: 返回用户创建的所有仓库的拉取请求总数。
        """
        user = self.get_user(username)
        total_prs = 0
        for repo in user.get_repos():
            # 获取仓库中所有状态为 'all' 的拉取请求
            prs = repo.get_pulls(state='all')
            # 过滤由指定用户创建的拉取请求
            for pr in prs:
                if pr.user.login == username:
                    total_prs += 1
        return total_prs

    def get_user_issues(self, username):
        """
        获取用户创建的问题总数。
        :param username: 用户名。
        :return: 返回用户在其所有仓库中报告的问题总数。
        """
        user = self.get_user(username)
        total_issues = 0
        for repo in user.get_repos():
            issues = repo.get_issues(creator=username)
            total_issues += issues.totalCount
        return total_issues

    def get_user_activity_stats(self, username):
        """
        获取用户的社区活动统计数据，包括提交次数、拉取请求、问题、接收的星标、分支和跟随者数。
        :param username: 用户名。
        :return: 包含各种社区活动统计的字典。
        """
        user = self.get_user(username)
        return {
            'total_commits': self.get_contributions(user),
            'total_pull_requests': self.get_user_pull_requests(username),
            'total_issues': self.get_user_issues(username),
            'total_stars_received': sum(repo.stargazers_count for repo in user.get_repos()),
            'total_forks_received': sum(repo.forks_count for repo in user.get_repos()),
            'followers_count': user.followers
        }

    def get_user_organizations(self, username):
        """
        获取一个用户所属的所有GitHub组织以及相关的统计数据。
        :param username: GitHub的用户名。
        :return: 列表，包含用户所属组织的相关数据；或者一个消息，说明用户不属于任何组织。
        """
        user = self.client.get_user(username)
        orgs = user.get_orgs()
        if orgs.totalCount == 0:
            return {"message": "This user does not belong to any organizations."}

        orgs_data = []
        for org in orgs:
            repos = list(org.get_repos())  # 获取组织下的所有仓库列表
            data = {
                'name': org.login,
                'repos': len(repos),  # 仓库数量
                'members': sum(1 for _ in org.get_public_members()),  # 公开成员数量
                'stars': sum(repo.stargazers_count for repo in repos),  # 所有仓库的星标总数
                'forks': sum(repo.forks_count for repo in repos),  # 所有仓库的Fork总数
                'watchers': sum(repo.watchers_count for repo in repos)  # 所有仓库的观察者总数
            }
            orgs_data.append(data)

        return orgs_data

