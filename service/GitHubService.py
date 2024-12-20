import requests
from flask import session

import config
from common.AssessCommon import assess
from common.Tool.GithubToolCommon import GitHubService
from common.Tool.MultiThreadHelperCommon import MultiThreadHelper
from common.scoreCommon import get_user_score

GITHUB_USER_API_URL = "https://api.github.com/user"


def verification_token(token):
    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(GITHUB_USER_API_URL, headers=headers)

    if response.status_code != 200:
        return {"error": response.text}, 401

    session['token'] = token
    config.GITHUB_ACCESS_TOKEN = session['token']

    # 获取用户信息
    user_info = response.json()
    user_name = user_info.get("login")
    user_avatar = user_info.get("avatar_url")
    # 返回用户的 name
    return {"name": user_name, "avatar_url": user_avatar}, 200


def get_user_info(username, token):
    headers = {
        "Authorization": f"token {token}"
    }
    user_api_url = f"{GITHUB_USER_API_URL}s/{username}"
    response = requests.get(user_api_url, headers=headers)

    # 如果请求失败，返回错误信息和状态码
    if response.status_code != 200:
        return "用户名错误!", response.status_code

    user_info = response.json()
    user_data = {
        "login": user_info.get("login"),
        "name": user_info.get("name"),
        "company": user_info.get("company"),
        "blog": user_info.get("blog"),
        "location": user_info.get("location"),
        "email": user_info.get("email"),
        "bio": user_info.get("bio"),
        "public_repos": user_info.get("public_repos"),
        "followers": user_info.get("followers"),
        "following": user_info.get("following"),
        "created_at": user_info.get("created_at"),
        "avatar_url": user_info.get("avatar_url"),
        "html_url": user_info.get("html_url")
    }
    g = GitHubService(token)
    helper = MultiThreadHelper(max_workers=3)
    future_score = helper.submit_task(get_user_score, username, token)
    future_country = helper.submit_task(g.get_location, username)
    future_bio = helper.submit_task(assess, username, token)
    user_data['score'] = future_score.result()
    user_data['country'], reliability = future_country.result()
    user_data['reliability'] = reliability
    user_data['bio'] = future_bio.result()

    # 成功时返回用户数据和状态码 200
    return user_data, 200
