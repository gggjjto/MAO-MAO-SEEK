import os
import re

import pandas as pd

# 用来对 cvs/github_rank.csv 中的大量原始数据进行分类，按照国家进行分类

github_rank_df = pd.read_csv('cvs/github_rank.csv')
processed_github_rank_df = pd.read_csv('cvs/processed_github_rank.csv')

merged_df = github_rank_df.merge(processed_github_rank_df[['login', 'location']], on='login',
                                 suffixes=('_original', '_country'))

grouped_by_country = merged_df.groupby('location_country')

output_directory = './country'
os.makedirs(output_directory, exist_ok=True)

for country, group in grouped_by_country:
    sanitized_country = re.sub(r'[^a-zA-Z0-9_一-鿿]', '_', country.strip())
    filename = f'{output_directory}/github_users_{sanitized_country}.csv'
    group.to_csv(filename, index=False)

print("分类完成，每个国家的数据已保存为单独的CSV文件。")
