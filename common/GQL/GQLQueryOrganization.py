overview_query = """
query($org_name: String!) {
  organization(login: $org_name) {
    name
    description
    websiteUrl
    email
    location
  }
}
"""

repositories_query = """
query($org_name: String!) {
  organization(login: $org_name) {
    repositories(first: 100) {
      nodes {
        name
        description
        url
      }
    }
  }
}
"""

projects_query = """
query($org_name: String!) {
  organization(login: $org_name) {
    projectsV2(first: 100) {
      nodes {
        title
        url
      }
    }
  }
}
"""

people_query = """
query($org_name: String!) {
  organization(login: $org_name) {
    membersWithRole(first: 100) {
      nodes {
        login
        name
      }
    }
  }
}
"""
