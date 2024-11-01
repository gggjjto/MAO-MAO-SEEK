from collections import Counter

import config
from common.GraphQLConfig import GraphQLConfig
from common.RedisCommon import redis_tool
from common.SendMessage import send_post_request


def get_associated_users(username):
    graphql_client = GraphQLConfig(config.GITHUB_ACCESS_TOKEN)

    # 获取用户的关注者和关注的人的位置信息
    locations = graphql_client.get_associated_users_locations(username)

    return locations


def extract_country_one(o):
    s = o.split(", ")[-1]
    # value = mp.get(s.lower())
    value = redis_tool.get_value(s.lower())
    if value is None:
        value = send_post_request(s.lower())
        redis_tool.set_value(s.lower(), value)
    return value


def extract_country(location):
    # mp = countries_map()
    country = []
    for o in location:
        value = extract_country_one(o)
        country.append(value)
    return country


def guess_nation(username):
    locations = get_associated_users(username)
    all_locations = locations['followers'] + locations['following']
    country = extract_country(all_locations)
    counts = Counter(country)
    max_country = max(counts.keys(), key=counts.get)
    return max_country.decode('utf-8'), counts.get(max_country) / len(country)
