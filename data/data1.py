import pandas as pd

from common.FromCountryCommon import extract_country_one

df = pd.read_csv('cvs/github_rank.csv')


# 对 cvs/github_rank.csv 中地名的信息进行转换

def get_location(s):
    a = extract_country_one(s)
    print(f'location:{s} = {a}')
    return a


df = df[df['location'].notna()]
df['location'] = df['location'].apply(get_location)

# 保存到新的CSV文件
df.to_csv('./processed_github_rank.csv', index=False)
