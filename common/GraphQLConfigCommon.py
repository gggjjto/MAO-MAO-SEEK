import time

import requests

from common.GQL.GQLQueryGitHub import associated_users_locations_query
from common.ProxyPoolCommon import proxy_pool


class GraphQLConfig:
    def __init__(self, access_token):
        self.api_url = "https://api.github.com/graphql"
        self.headers = {'Authorization': f'Bearer {access_token}'}

    def execute_query(self, query, variables=None):
        # 发送grapql api请求
        # time.sleep(10)  # 暂停一下
        proxy = proxy_pool()
        response = requests.post(self.api_url, json={'query': query, 'variables': variables}, proxies={"http": proxy},
                                 headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Query failed to run by returning code of {}. {}".format(response.status_code, response.text))
            return None

    def get_associated_users_locations(self, username):
        """
        根据用户名获取关注用户和被关注用户位置信息。
        :param username: GitHub用户名。
        :return: 用户对象。
        """
        query = associated_users_locations_query
        variables = {"username": username}
        data = self.execute_query(query, variables)
        # print(data)
        if data and 'data' in data and 'user' in data['data']:
            locations = {
                'followers': [node['location'] for node in data['data']['user']['followers']['nodes'] if
                              node['location']],
                'following': [node['location'] for node in data['data']['user']['following']['nodes'] if
                              node['location']]
            }
            return locations
        return None

    def github_graphql(self, query, username):
        variables = {"username": username}
        data = self.execute_query(query, variables)
        return data

    def send_query(self, query, variables):
        data = self.execute_query(query, variables)
        return data
