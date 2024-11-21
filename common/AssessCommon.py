import requests
from bs4 import BeautifulSoup

from common.Tool.GPTToolCommon import send_assess


def fetch_user_blog(username, token):
    # 抓取个人网站网址
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


def fetch_readme_via_api(username, token):
    # 抓取用户的个人介绍仓库
    api_url = f"https://api.github.com/repos/{username}/{username}/readme"
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


def fetch_github_pages(url):
    # 抓取个人网址
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
    # 获取最后的评价
    try:
        blog_url, status_code = fetch_user_blog(username, token)
        readme_data, readme_status_code = fetch_readme_via_api(username, token)
        if status_code == 200:
            blog_data, status_code = fetch_github_pages(blog_url)
            if status_code == 200:
                data = blog_data + blog_data
                s = send_assess(data)
                return s
        if readme_status_code == 200:
            s = send_assess(readme_data)
            return s
        return None
    except:
        return None
