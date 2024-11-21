import requests
from flask import session


def get_repository_languages(owner, repo_name):
    # 查询仓库使用的语言
    token = session['token']
    url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # 返回的 JSON 对象包含语言和对应的代码字节数
    else:
        return f"Error: {response.status_code}"


def send_response(url, headers, params):
    # 一个发送请求的函数
    response = requests.get(url, headers=headers, params=params, verify=True)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return response.status_code
