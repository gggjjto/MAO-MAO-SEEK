from flask import request, jsonify

from service.GithubService import *


def github_routes(app):
    @app.route('/login', methods=['GET'])
    def login():
        # 获取 GET 请求中的 token 参数
        token = request.args.get('token')
        if not token:
            return jsonify({"error": "Token 不存在"}), 400

        data, status_code = verification_token(token)
        # 如果验证失败，返回错误响应
        if status_code != 200:
            return jsonify(data), status_code

        return jsonify(data)

    @app.route('/user', methods=['GET'])
    def get_user():
        username = request.args.get('username')
        token = session.get('token')
        if not token:
            return jsonify({"error": "没有输入GitHub_Token"}), 401
        if not username:
            return jsonify({"error": "错误的用户名"}), 400

        data, status_code = get_user_info(username, token)

        return jsonify(data), status_code

    # @app.route('/user/<username>', methods=['GET'])
    # def get_user(username):
    #     # 根据用户名获取用户对象
    #     github_service = GitHubService(session['github_token'])
    #     user = github_service.get_user(username)
    #     return jsonify({
    #         'login': user.login,
    #         'name': user.name,
    #         'public_repos': user.public_repos,
    #         'followers': user.followers,
    #         'following': user.following
    #     })
    #
    # @app.route('/user/<username>/repos', methods=['GET'])
    # def get_user_repositories(username):
    #     # 获取用户贡献的仓库及其星标数。
    #     github_service = GitHubService(session['github_token'])
    #     repos = github_service.get_contributed_repos_stars(username)
    #     return jsonify(repos)
    #
    # @app.route('/user/<username>/activity', methods=['GET'])
    # def get_user_activity(username):
    #     # 获取用户的社区活动统计数据，包括提交次数、拉取请求、问题、接收的星标、分支和跟随者数。
    #     github_service = GitHubService(session['github_token'])
    #     activity_stats = github_service.get_user_activity_stats(username)
    #     return jsonify(activity_stats)
    #
    # @app.route('/user/<username>/languages', methods=['GET'])
    # def get_user_languages(username):
    #     # 获取指定用户的所有仓库中使用的编程语言及其代码行数。
    #     github_service = GitHubService(session['github_token'])
    #     languages = github_service.get_fetch_languages(username)
    #     return jsonify(dict(languages))
    #
    # @app.route('/organization/<username>/influence', methods=['GET'])
    # def get_organization_influence(username):
    #     # 获取一个用户所属的所有GitHub组织以及相关的统计数据。
    #     github_service = GitHubService(session['github_token'])
    #     influence_data = github_service.get_user_organizations(username)
    #     if influence_data:
    #         return jsonify(influence_data)
    #     else:
    #         return jsonify({'error': 'Organization not found or has no data'}), 404

    # @app.route('/get_score/<username>', methods=['GET'])
    # def get_score(username):
    #     score = display_user_contributions(username)
    #     return jsonify(score)

    # @app.route('/set_token', methods=['POST'])
    # def set_token():
    #     token = request.json.get('token')
    #     if token:
    #         session['github_token'] = token
    #         try:
    #             remaining_limit = get_rate_limit(token)
    #             if remaining_limit > 0:
    #                 return jsonify({'message': f'Token set successfully'}), 200
    #             else:
    #                 return jsonify({'message': f'Token set failed'}), 401
    #         except Exception as e:
    #             return jsonify({'error': 'No token provided'}), 400
    #     else:
    #         return jsonify({'error': 'No token provided'}), 400
