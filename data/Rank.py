import argparse
import os
import re

import pandas as pd

from common.FromCountryCommon import extract_country_one
from common.Tool.RedisCommon import RedisTool
from common.scoreCommon import get_score


def process_locations(input_file, output_file):
    """
    处理 location 数据
    """
    if os.path.exists(output_file):
        print(f"{output_file} 已存在，跳过处理 location。")
        return
    df = pd.read_csv(input_file)
    df = df[df['location'].notna()]
    df['location'] = df['location'].apply(lambda s: extract_country_one(s))
    df.to_csv(output_file, index=False)
    print(f"Location 处理完成，保存至 {output_file}。")


def categorize_by_country(input_file, output_directory):
    """
    按国家分类数据
    """
    if os.path.exists(output_directory):
        print(f"{output_directory} 目录已存在，跳过国家分类。")
        return
    os.makedirs(output_directory, exist_ok=True)
    df = pd.read_csv(input_file)
    grouped = df.groupby('location_country')
    for country, group in grouped:
        sanitized_country = re.sub(r'[^a-zA-Z0-9_一-鿿]', '_', country.strip())
        filename = f"{output_directory}/github_users_{sanitized_country}.csv"
        group.to_csv(filename, index=False)
    print(f"按国家分类完成，数据已保存至 {output_directory}。")


def process_scores(input_file, output_file, token):
    """
    计算用户分数
    """
    if os.path.exists(output_file):
        print(f"{output_file} 已存在，跳过分数处理。")
        return
    df = pd.read_csv(input_file)
    redis = RedisTool(db=1)

    def get_score_1(login):
        score = redis.get_value(login)
        if score is None:
            score = get_score(login, token)
            redis.set_value(login, score)
        print(f"login:{login} - score = {score}")
        return score

    df['score'] = df.apply(lambda row: get_score_1(row['login']), axis=1)
    df.to_csv(output_file, index=False)
    print(f"分数处理完成，保存至 {output_file}。")


def generate_ts(input_file, output_directory, country="中国"):
    """
    导出数据为 TypeScript 文件
    """
    if not os.path.exists(input_file):
        print(f"{input_file} 不存在，无法生成 TypeScript 文件。")
        return
    os.makedirs(output_directory, exist_ok=True)
    df = pd.read_csv(input_file)

    if 'location_original' in df.columns:
        df.rename(columns={'location_original': 'location'}, inplace=True)

    required_columns = ['login', 'name', 'location', 'followers', 'repositories', 'score']
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0

    sorted_df = df.sort_values(by='score', ascending=False).head(100)

    headers = """
interface Header {
  key: string
  title: string
  align?: 'start' | 'center' | 'end'
  sortable?: boolean
  value?: string // 用于标识字段名称，可能替代 key
}

export const headers: Header[] = [
  {
    align: 'start',
    key: 'login',
    sortable: false,
    title: '开发者(前100名)', 
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
    data_array = "export const desserts = ref<Dessert[]>([\n"
    for _, row in sorted_df.iterrows():
        data_array += f"  {{ login: '{row['login']}', name: '{row['name']}', location: '{row['location']}', followers: {row['followers']}, repositories: {row['repositories']}, score: {row['score']} }},\n"
    data_array += "]);\n"

    ts_file_path = os.path.join(output_directory, f"github_rank_{country}.ts")
    with open(ts_file_path, 'w', encoding='utf-8') as ts_file:
        ts_file.write(headers)
        ts_file.write('\n')
        ts_file.write(data_array)

    print(f"TypeScript 文件已生成，保存至 {ts_file_path}。")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="整合多个功能并执行。")
    parser.add_argument('--input', default='cvs/github_rank.csv', help="输入的原始 CSV 文件路径")
    parser.add_argument('--processed', default='cvs/processed_github_rank_1.csv', help="处理后的 CSV 文件路径")
    parser.add_argument('--country_dir', default='./country', help="按国家分类的输出目录")
    parser.add_argument('--country_file', default='./country/github_users_中国.csv', help="需要生成的国家文件")
    parser.add_argument('--scored', default='./processed_github_rank_2.csv', help="包含分数的 CSV 文件路径")
    parser.add_argument('--ts_dir', default='./TS', help="TypeScript 输出目录")

    args = parser.parse_args()
    token = ""  # GitHub api token

    try:
        process_locations(args.input, args.processed)
        categorize_by_country(args.processed, args.country_dir)
        process_scores(args.country_file, args.scored, token)
        generate_ts(args.scored, args.ts_dir)
    except Exception as e:
        print(f"程序执行过程中出现错误: {e}")
        exit(1)

"""
python Rank.py --input cvs/github_rank.csv 
                      --processed cvs/processed_github_rank_1.csv 
                      --country_dir ./country 
                      --country_file ./country/github_users_中国.csv
                      --scored ./processed_github_rank_2.csv 
                      --ts_dir ./TS
"""
