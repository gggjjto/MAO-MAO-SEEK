gql_pinned_repos = """
    query($username: String!) {
      user(login: $username) {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              owner {
                login
              }
              defaultBranchRef {
                name
              }
            }
          }
        }
      }
    }
    """