import re

import config
from common.Tool.GPTToolCommon import gpt_send, set_message
from common.GraphQLConfigCommon import GraphQLConfig
from common.Tool.MultiThreadHelperCommon import MultiThreadHelper
from common.Tool.RedisCommon import redis_tool


def get_associated_users(username):
    # 查询获取用户的关注者和关注的人的位置信息
    graphql_client = GraphQLConfig(config.GITHUB_ACCESS_TOKEN)
    # 获取用户的关注者和关注的人的位置信息
    locations = graphql_client.get_associated_users_locations(username)

    return locations


def extract_country_one(o):
    # 尝试分割地名，尝试重redis中查找
    s = o.split(", ")[-1]
    o = o.lower()
    s = s.lower()
    value = redis_tool.get_value(s)
    if value is None:
        value = redis_tool.get_value(o)
        if value is None:
            value = gpt_send(set_message(o))
            redis_tool.set_value(o, value)
        redis_tool.set_value(s, value)
    return value


def extract_country(location):
    # 根据地名查找国家
    multi_thread_helper = MultiThreadHelper()
    futures = []
    for o in location:
        # 使用多线程
        futures.append(multi_thread_helper.submit_task(extract_country_one, o))
    results = multi_thread_helper.wait_for_all(futures)
    return results


def guess_nation(username):
    # 猜测开发者位于的国家
    locations = get_associated_users(username)
    all_locations = locations['followers'] + locations['following']
    try:
        data = set_message(str(all_locations))
        match = re.search(r'\[国家名：(.*?)，置信度：(.*?)\]', data)
        country = match.group(1)
        confidence = float(match.group(2))  # 转换为浮点数
        if confidence < 0.6:
            country = 'N/A'
        return country, confidence
    except:
        return 'N/A', 0


if __name__ == '__main__':
    country, confidence = guess_nation('lmxue')
    print(country, confidence)
