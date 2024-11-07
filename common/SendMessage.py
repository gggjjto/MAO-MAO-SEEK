import time

import requests

import config
from common.ProxyPool import proxy_pool


def get_repository_languages(owner, repo_name):
    # 查询仓库使用的语言
    url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
    headers = {
        'Authorization': f'Bearer {config.GITHUB_ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # 返回的 JSON 对象包含语言和对应的代码字节数
    else:
        return f"Error: {response.status_code}"


def send_response(url, headers, params):
    # 一个发送请求的函数
    time.sleep(5)
    proxy = proxy_pool()
    response = requests.get(url, headers=headers, proxies={"http": proxy}, params=params, verify=True)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return response.status_code
