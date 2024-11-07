import random


def proxy_pool():
    # 代理池，随机返回一个代理
    proxies = [
        "http://47.116.181.146:8800",
        "http://61.129.2.212:8080",
        "http://47.108.159.113:8008",
        "http://47.122.31.238:80",
        "http://39.102.213.187:8443",
        "http://39.102.209.121:8081"
        "http://39.104.16.201:8080",
        "http://47.105.122.72:9080",
        "http://47.92.143.92:80",
        "http://39.102.213.3:8008",
        "http://39.101.132.59:8443",
        "http://47.122.5.165:4006",
        "http://47.119.164.33:8080",
        "http://39.102.210.176:3128"
    ]

    proxy = random.choice(proxies)
    return proxy