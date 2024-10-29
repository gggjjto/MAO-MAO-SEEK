from flask import request, jsonify

from service.CalculateScore import display_user_contributions
from service.GitHubService import GitHubService


def github_routes(app):

    github_service = GitHubService()

    @app.route('/user/<username>', methods=['GET'])
    def get_user(username):
        # 根据用户名获取用户对象
        user = github_service.get_user(username)
        return jsonify({
            'login': user.login,
            'name': user.name,
            'public_repos': user.public_repos,
            'followers': user.followers,
            'following': user.following
        })

    @app.route('/user/<username>/repos', methods=['GET'])
    def get_user_repositories(username):
        # 获取用户贡献的仓库及其星标数。
        repos = github_service.get_contributed_repos_stars(username)
        return jsonify(repos)

    @app.route('/user/<username>/activity', methods=['GET'])
    def get_user_activity(username):
        # 获取用户的社区活动统计数据，包括提交次数、拉取请求、问题、接收的星标、分支和跟随者数。
        activity_stats = github_service.get_user_activity_stats(username)
        return jsonify(activity_stats)

    @app.route('/user/<username>/languages', methods=['GET'])
    def get_user_languages(username):
        # 获取指定用户的所有仓库中使用的编程语言及其代码行数。
        languages = github_service.get_fetch_languages(username)
        return jsonify(dict(languages))

    @app.route('/organization/<username>/influence', methods=['GET'])
    def get_organization_influence(username):
        # 获取一个用户所属的所有GitHub组织以及相关的统计数据。
        influence_data = github_service.get_user_organizations(username)
        if influence_data:
            return jsonify(influence_data)
        else:
            return jsonify({'error': 'Organization not found or has no data'}), 404

    @app.route('/get_score/<username>', methods=['GET'])
    def get_score(username):
        score = display_user_contributions(username)
        return jsonify(score)
