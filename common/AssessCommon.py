import requests
from bs4 import BeautifulSoup

import config
from common.Tool.GPTToolCommon import send_assess
from common.Tool.GithubToolCommon import GitHubService
from common.Tool.MultiThreadHelperCommon import MultiThreadHelper


def fetch_user_blog(username, token):
    # 个人网站网址
    api_url = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}"
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        blog_url = user_data.get('blog', '')
        if blog_url:
            print(f"用户 {username} 的个人网站链接：{blog_url}")
            return blog_url, 200
        else:
            print(f"用户 {username} 没有提供个人网站链接。")
            return None, 500
    else:
        print(f"无法获取用户信息，状态码：{response.status_code}")
        return None, 500


def fetch_readme_api(owner, repo, token):
    # 用户的仓库介绍
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {
        "Accept": "application/vnd.github.v3.raw",
        "Authorization": f"token {token}"
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        readme_content = response.text
        print("README.md 已成功通过 GitHub API 抓取并保存为 README_API.md")
        return readme_content, 200
    else:
        print(f"无法获取 README.md，状态码：{response.status_code}")
        return None, 500


def fetch_pinned_readme(username, token):
    # 获取pinned仓库介绍
    g = GitHubService(token)
    pinned_repos = g.fetch_pinned_repos(username)
    data = ""
    if not pinned_repos:
        print(f"{username} 没有 Pinned 项目。")
        return

    print(f"\n{username} 的 Pinned 仓库及 README 内容：")
    for repo in pinned_repos:
        repo_name = repo.get("name")
        owner = repo.get("owner", {}).get("login")
        # default_branch = repo.get("defaultBranchRef", {}).get("name", "main")

        print(f"\n仓库: {owner}/{repo_name}")
        readme_content, code = fetch_readme_api(owner, repo_name, token)
        if code == 200:
            print("README 内容：")
            print(readme_content)
            data += repo_name + ":" + readme_content + ";"
        else:
            print("README.md 文件不存在或无法读取。")
            data += repo_name + ": '' ;"
    return data


def fetch_github_pages(url):
    # 个人网址
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.HTTPError as err:
        print(f"HTTP 错误：{err}")
        return None, 500
    except Exception as err:
        print(f"其他错误：{err}")
        return None, 500

    soup = BeautifulSoup(response.text, 'html.parser')

    # 移除脚本和样式内容
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()

    # 获取纯文本
    text = soup.get_text(separator='\n')

    # 清理文本：去除多余的空行和空格
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text, 200


def assess(username, token):

    # 定义任务函数
    def fetch_blog():
        try:
            return fetch_user_blog(username, token)
        except Exception as e:
            print(f"获取博客数据时发生错误: {e}")
            return None, None

    def fetch_readme():
        try:
            return fetch_readme_api(username, username, token)
        except Exception as e:
            print(f"获取 README 数据时发生错误: {e}")
            return None, None

    def fetch_pinned():
        try:
            return fetch_pinned_readme(username, token)
        except Exception as e:
            print(f"获取 Pinned 数据时发生错误: {e}")
            return ""


    # 初始化多线程工具类
    helper = MultiThreadHelper(max_workers=3)

    # 提交任务
    future_blog = helper.submit_task(fetch_blog)
    future_readme = helper.submit_task(fetch_readme)
    future_pinned = helper.submit_task(fetch_pinned)

    # 等待任务完成
    blog_result = future_blog.result()
    readme_result = future_readme.result()
    pinned_result = future_pinned.result()


    # 获取最后的评价
    try:
        blog_url, status_code = blog_result
        readme_data, readme_status_code = readme_result
        pinned_data = pinned_result
        blog_data = ""
        if status_code == 200:
            blog_data, status_code = fetch_github_pages(blog_url)
        if readme_status_code != 200:
            readme_data = ""
        data = blog_data + readme_data + pinned_data
        s = send_assess(data)
        return s
    except Exception as e:
        print(f"评估过程中发生错误: {e}")
        return None


if __name__ == '__main__':
    data = assess('torvalds', config.GITHUB_ACCESS_TOKEN)
    print(data)