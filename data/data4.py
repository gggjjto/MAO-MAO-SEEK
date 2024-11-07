import pandas as pd


processed_github_rank1_df = pd.read_csv('./csv/processed_github_rank1.csv')


github_users_china_df = pd.read_csv('./country/github_users_中国.csv')


merged_china_df = github_users_china_df.merge(processed_github_rank1_df[['login', 'score']], on='login', how='left')


merged_china_df.to_csv('./country/github_users_中国.csv', index=False)

print("中国用户数据已更新，包含分数信息。")
