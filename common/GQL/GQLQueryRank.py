process_rank_query = """
query ($query: String!, $first: Int!, $after: String) {
  search(query: $query, type: USER, first: $first, after: $after) {
    userCount
    edges {
      node {
        ... on User {
          login
          name
          location
          createdAt
          followers {
            totalCount
          }
          repositories {
            totalCount
          }
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""
