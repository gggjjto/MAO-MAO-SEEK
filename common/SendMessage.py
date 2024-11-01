import requests

import config


def send_post_request(message):
    url = "https://api.binjie.fun/api/generateStream?refer__1360=eqmxuDB7i%3DD%3DqBIKGNDQuAEbGDkKDgDUDOGoD"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Referer": "https://chat18.aichatos98.com/",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": "https://chat18.aichatos98.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }

    data = {
        "prompt": f"{message}这是那个国家，直接说国家名字就可以了",
        "userId": "#/chat/1730276151521",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }

    # 发送 POST 请求
    response = requests.post(url, json=data, headers=headers)

    # 检查响应
    if response.status_code == 200:
        response.encoding = 'utf-8'
        # print(f"{message}-Success:", response.text)
        return response.text.replace('。', '')
    else:
        print("Failed to send request. Status code:", response.status_code, "Response:", response.text)


def get_repository_languages(owner, repo_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
    headers = {
        'Authorization': f'Bearer {config.GITHUB_ACCESS_TOKEN}',  # 替换 YOUR_GITHUB_TOKEN 为你的 GitHub Access Token
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # 返回的 JSON 对象包含语言和对应的代码字节数
    else:
        return f"Error: {response.status_code}"