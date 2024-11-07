from collections import Counter

import config
from common.GPTTool import gpt_send, set_message
from common.GraphQLConfig import GraphQLConfig
from common.MultiThreadHelper import MultiThreadHelper
from common.RedisCommon import redis_tool, RedisTool


def get_associated_users(username):
    # 查询获取用户的关注者和关注的人的位置信息，并做缓存
    graphql_client = GraphQLConfig(config.GITHUB_ACCESS_TOKEN)
    r = RedisTool(db=2)
    locations = r.get_value(username)
    if locations is None:
        # 获取用户的关注者和关注的人的位置信息
        locations = graphql_client.get_associated_users_locations(username)
        # r.set_json(username, locations)
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
    multi_thread_helper = MultiThreadHelper(max_workers=20)
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
    country = extract_country(all_locations)
    counts = Counter(country)
    max_country = max(counts.keys(), key=counts.get)
    return max_country, counts.get(max_country) / len(country)
