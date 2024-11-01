from common.GQL.GQLQueryOrganization import *
from common.GraphQLConfig import *
import config


class OrganizationService:
    def __init__(self, org_name):
        self.org_name = org_name
        self.variables = {"org_name": org_name}
        self.client = GraphQLConfig(config.GITHUB_ACCESS_TOKEN)

    def get_organization_overview(self):
        """
        获取组织概述
        :return: 返回组织name、description、websiteUrl、email、location
        """
        result = self.client.send_query(overview_query, self.variables)
        if result and "data" in result:
            return result["data"]["organization"]
        return None

    def get_organization_repositories(self):
        """
        获取仓库列表
        :return: 组织仓库、描述、url
        """
        result = self.client.send_query(repositories_query, self.variables)
        if result and "data" in result:
            return result["data"]["organization"]["repositories"]["nodes"]
        return None

    def get_organization_people(self):
        """
        获取组织成员
        :return: 组织成员
        """
        result = self.client.send_query(people_query, self.variables)
        if result and "data" in result:
            return result["data"]["organization"]["membersWithRole"]["nodes"]
        return None
