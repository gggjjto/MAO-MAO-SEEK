import pandas as pd

# 读取 CSV 文件
file_path = './cvs/processed_github_rank.csv'  # 替换为你自己的文件路径
df = pd.read_csv(file_path)

# 筛选国家为中国的用户
df_china = df[df['location'] == '中国']

# 显示结果
df_china.reset_index(drop=True, inplace=True)
print(df_china)

# 可选：保存筛选后的结果到新的 CSV 文件
df_china.to_csv('./china_users.csv', index=False)
