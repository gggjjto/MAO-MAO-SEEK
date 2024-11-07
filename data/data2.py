import pandas as pd

from common.RedisCommon import RedisTool
from common.scoreCommon import get_score

df = pd.read_csv('cvs/china_users.csv')

redis = RedisTool(db=1)


def get_score1(login):
    score = redis.get_value(login)
    if score is None:
        score = get_score(login)
        redis.set_value(login, score)
    print(f'login:{login} - score = {score}')
    return score


df['score'] = df.apply(lambda row: get_score1(row['login']), axis=1)

# 保存到新的CSV文件
df.to_csv('./processed_github_rank1.csv', index=False)
