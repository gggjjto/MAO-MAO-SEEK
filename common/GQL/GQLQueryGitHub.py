associated_users_locations_query = """
query($username: String!) {
  user(login: $username) {
    followers(first: 100) {
      nodes {
        location
      }
    }
    following(first: 100) {
      nodes {
        location
      }
    }
  }
}
"""

user_query = """
query ($username: String!) {
  user(login: $username) {
    login
    name
    repositories {
      totalCount
    }
    followers {
      totalCount
    }
    following {
      totalCount
    }
    location
  }
}
"""

get_repositories_query = """
query ($username: String!) {
  user(login: $username) {
    repositories(first: 100, privacy: PUBLIC, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes {
        name
        isPrivate
        stargazerCount
        forkCount
        description
        watchers{
            totalCount
        }
      }
    }
  }
}
"""

get_organizations_query = """
query ($username: String!) {
  user(login: $username) {
    organizations(first: 100) {
      nodes {
        name
        url
        description
      }
    }
  }
}
"""

get_contributions_query = """
    query GetUserYearlyContributions($username: String!) {
      user(login: $username) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
"""

get_repository_contributions_query = """
query($owner: String!, $repo: String!) {
    repository(owner: $owner, name: $repo) {
        collaborators {
            totalCount
        }
    }
}
"""

get_contributed_query = """
query GetUserRepositories($username: String!){
  user(login: $username) {
    repositories(first: 100, privacy: PUBLIC) {
      totalCount
      nodes {
        name
        owner {
          login
        }
        stargazers {
          totalCount
        }
        url
        isFork
      }
    }
  }
}
"""

get_fetch_languages_query = """
query($username: String!) {
  user(login: $username) {
    repositories(first: 100, affiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER]) {
      nodes {
        languages(first: 10) {
          edges {
            size
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

get_user_pull_requests_query = """
query($username: String!) {
  user(login: $username) {
    pullRequests(first: 100, states: OPEN) {
      totalCount
    }
  }
}
"""

get_user_issues_query = """
query($username: String!) {
  user(login: $username) {
    issues(first: 100, filterBy: {createdBy: $username}) {
      totalCount
    }
  }
}
"""

get_user_activity_stats_query = """
query($username: String!) {
  user(login: $username) {
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
    }
    pullRequests(first: 0) {
      totalCount
    }
    issues(first: 0) {
      totalCount
    }
    repositories(first: 100) {
      totalCount
      nodes {
        stargazers {
          totalCount
        }
        forkCount
      }
    }
    followers {
      totalCount
    }
  }
}
"""

get_user_organizations_query = """
query($username: String!) {
  user(login: $username) {
    organizations(first: 100) {
      totalCount
      nodes {
        name
        login
        repositories(first: 1, affiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER]) {
          totalCount
        }
        membersWithRole(first: 1) {
          totalCount
        }
        repository(name: "name_of_the_repository") {
          stargazers {
            totalCount
          }
          forks {
            totalCount
          }
          watchers {
            totalCount
          }
        }
      }
    }
  }
}
"""
