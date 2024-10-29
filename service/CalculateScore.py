from service.GitHubService import GitHubService


def calculate_total_score(data):
    weights = {
        'commits': 0.20,
        'followers': 0.15,
        'total_stars': 0.20,
        'total_forks': 0.15,
        'organization_influence': 0.10,
        'language_diversity': 0.10,
        'individual_project_influence': 0.10
    }

    # 示例数据中的值
    commits_score = min(data['total_commits'] / 50000, 1)  # 假设50,000为最高提交数
    followers_score = min(data['followers_count'] / 250000, 1)  # 假设250,000为最高跟随者数
    total_stars_score = min(data['total_stars_received'] / 200000, 1)  # 假设200,000为最高星标数
    total_forks_score = min(data['total_forks_received'] / 60000, 1)  # 假设60,000为最高Forks数

    # 组织影响力：取最大的一个组织作为评分标准
    organization_influence_score = min(max(org['stars'] for org in data['organizations']) / 1000, 1)

    # 编程语言多样性
    language_diversity_score = min(len(data['languages']) / 20, 1)  # 假设20种不同的语言为最高

    # 个别项目影响力：考虑每个项目的星标和贡献比例
    individual_project_influence_score = sum(
        min(proj[1] * (proj[2] / 100), 1000) for proj in data['projects']) / 10000

    # 计算总分
    total_score = (
                          weights['commits'] * commits_score +
                          weights['followers'] * followers_score +
                          weights['total_stars'] * total_stars_score +
                          weights['total_forks'] * total_forks_score +
                          weights['organization_influence'] * organization_influence_score +
                          weights['language_diversity'] * language_diversity_score +
                          weights['individual_project_influence'] * individual_project_influence_score
                  ) * 100  # 转换为百分制

    return total_score


def display_user_contributions(username):
    github_service = GitHubService()

    activity_stats = github_service.get_user_activity_stats(username)

    repos = github_service.get_contributed_repos_stars(username)

    language_stats = github_service.get_fetch_languages(username)

    stats = github_service.get_user_organizations(username)

    data = {
        'total_commits': activity_stats['total_commits'],
        'followers_count': activity_stats['followers_count'],
        'total_stars_received': activity_stats['total_stars_received'],
        'total_forks_received': activity_stats['total_forks_received'],
        'organizations': stats,
        'languages': language_stats,
        'projects': repos
    }

    score = calculate_total_score(data)
    return score
