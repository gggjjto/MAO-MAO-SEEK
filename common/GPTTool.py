import time

import requests

import config
from common.ProxyPool import proxy_pool


def gpt_send(message):
    # 查询阿里云百炼模型
    proxy = proxy_pool()
    time.sleep(6)
    # 创建一个带代理的请求会话
    # 设置 API Key 和请求 URL
    api_key = "YOUR_DASHSCOPE_API_KEY"  # 请替换为您的实际 API Key
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {config.DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }

    # 设置请求体
    data = {
        "model": "qwen-plus",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"{message}"
            }
        ]
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data, proxies={"http": proxy})

    # 检查请求的结果
    if response.status_code == 200:
        response_json = response.json()
        a = response_json['choices'][0]['message']['content']
        print(f"阿里云百炼模型返回的数据是：{a}")
        return a;
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


def set_message(message):
    # 按照地名查询国家
    s = f'地名：{message} 根据我给出的地名，告诉我这是那个国家，只要说国家名就可以了,如果不清楚就直接说：这不是一个国家'
    return s
