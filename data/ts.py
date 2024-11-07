# Import necessary libraries
import os

import pandas as pd

# Load the China-specific GitHub users data
github_users_china_df = pd.read_csv('./country/github_users_中国.csv')

# Rename 'location_original' column to 'location' if it exists
if 'location_original' in github_users_china_df.columns:
    github_users_china_df.rename(columns={'location_original': 'location'}, inplace=True)

# Ensure all necessary columns exist and handle missing values if necessary
required_columns = ['login', 'name', 'location', 'followers', 'repositories', 'score']
for col in required_columns:
    if col not in github_users_china_df.columns:
        github_users_china_df[col] = 0  # Add missing column with default value 0

# Sort the China-specific data by score in descending order and select the top 100
sorted_china_df = github_users_china_df.sort_values(by='score', ascending=False).head(100)

# Generate TypeScript header and data representation
headers = """
interface Header {
  key: string
  title: string
  align?: 'start' | 'center' | 'end'
  sortable?: boolean
  value?: string // 用于标识字段名称，可能替代 key
}

const headers: Header[] = [
  {
    align: 'start',
    key: 'login',
    sortable: false,
    title: '中国开发者(前100名)',
  },
  { key: 'name', title: '网名' },
  { key: 'location', title: '位置信息' },
  { key: 'followers', title: '追随者数量' },
  { key: 'repositories', title: '仓库数量' },
  { key: 'score', title: '评分' },
];

interface Dessert {
  login: string
  name: string
  location: string
  followers: number
  repositories: number
  score: number
}
"""

data_array = "const desserts = ref<Dessert[]>([\n"
for _, row in sorted_china_df.iterrows():
    data_array += f"  {{ login: '{row['login']}', name: '{row['name']}', location: '{row['location']}', followers: {row['followers']}, repositories: {row['repositories']}, score: {row['score']} }},\n"
data_array += "]);\n"

# Save TypeScript data to a file
output_directory = './TS'
os.makedirs(output_directory, exist_ok=True)
with open(f'{output_directory}/github_rank_China.ts', 'w', encoding='utf-8') as ts_file:
    ts_file.write(headers)
    ts_file.write('\n')
    ts_file.write(data_array)

print("TypeScript 文件已生成，包含中国开发者前100名的数据。")
