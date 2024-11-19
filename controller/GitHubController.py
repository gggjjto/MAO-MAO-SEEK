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