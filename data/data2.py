import pandas as pd


import config
from common.RedisCommon import RedisTool
from common.scoreCommon import get_score

df = pd.read_csv('country/github_users_美国.csv')

redis = RedisTool(db=1)

# 对文件进行分数统计

def get_score_1(login):
    score = redis.get_value(login)
    if score is None:
        score = get_score(login)
        redis.set_value(login, score)
    print(f'login:{login} - score = {score}')
    return score


df['score'] = df.apply(lambda row: get_score_1(row['login']), axis=1)

# 保存到新的CSV文件
df.to_csv('./processed_github_rank1.csv', index=False)
