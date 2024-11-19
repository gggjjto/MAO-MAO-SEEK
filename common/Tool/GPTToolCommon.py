import requests

import config
from common.Tool.ProxyPoolCommon import proxy_pool


def gpt_send(message):
    # 查询阿里云百炼模型
    proxy = proxy_pool()
    # time.sleep(6)
    # 创建一个带代理的请求会话
    # 设置 API Key 和请求 URL
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
    s = f'地名：{message} 这是github上开发者的关注者的位置信息，你来猜测开发者位于那个国家，只要返回两个值，一个是国家名，一个是猜测的置信度, 你返回的数据应该满足以下格式：[国家名：?，置信度：?]'
    data = gpt_send(s)
    return data


def send_assess(message):
    s = f"信息：{message} 根据我给出的信息整理出开发者评估信息, 返回中文, 返回100-200字的内容即可"
    data = gpt_send(s)
    return data
