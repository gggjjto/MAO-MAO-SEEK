import config
from data.source.DataHandlerCommon import DataHandler
from common.GQL.GQLQueryRank import process_rank_query
from common.GraphQLConfigCommon import GraphQLConfig


class Rank:
    def __init__(self, token):
        self.query = "followers:>1000 sort:followers-desc"
        self.first = 10
        self.cursor = None
        self.has_next_page = True
        self.client = GraphQLConfig(token)
        self.graphql_query = process_rank_query

    def query_gql(self):
        data = DataHandler()
        while self.has_next_page:
            variables = {
                "query": self.query,
                "first": self.first,
                "after": self.cursor
            }

            response = self.client.send_query(self.graphql_query, variables)

            if not response or "data" not in response:
                print("响应错误或缺少 'data' 字段。")
                break

            search_data = response['data'].get('search')
            if not search_data:
                print("响应中未找到 'search' 数据。")
                break

            edges = search_data.get('edges', [])
            if not edges:
                print("此批次未找到用户。")
                break

            for edge in edges:
                user = edge['node']
                if user:
                    user_data = {
                        'login': user.get('login', 'N/A'),
                        'name': user.get('name', 'N/A'),
                        'location': user.get('location', 'N/A'),
                        'followers': user.get('followers', {}).get('totalCount', 0),
                        'repositories': user.get('repositories', {}).get('totalCount', 0),
                        'created_at': user.get('created_at', 'N/A'),
                    }
                    data.write_user_data(user_data)

            page_info = search_data.get('pageInfo', {})
            self.has_next_page = page_info.get('hasNextPage', False)
            self.cursor = page_info.get('endCursor')

            print(f"下一个游标: {self.cursor}, 是否有下一页: {self.has_next_page}\n")


if __name__ == "__main__":
    GITHUB_ACCESS_TOKEN = config.GITHUB_ACCESS_TOKEN

    if not GITHUB_ACCESS_TOKEN:
        print("错误: config.py 中未设置 GITHUB_ACCESS_TOKEN")
    else:
        rank = Rank(GITHUB_ACCESS_TOKEN)
        rank.query_gql()
