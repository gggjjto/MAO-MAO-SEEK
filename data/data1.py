import pandas as pd

from common.FromCountryCommon import extract_country_one

df = pd.read_csv('cvs/github_rank.csv')


def get_location(s):
    a = extract_country_one(s)
    print(f'location:{s} = {a}')
    return a


df = df[df['location'].notna()]
df['location'] = df['location'].apply(get_location)

# df['score'] = df.apply(lambda row: get_score(row['login'], row['followers']), axis=1)

# 保存到新的CSV文件
df.to_csv('./processed_github_rank.csv', index=False)
