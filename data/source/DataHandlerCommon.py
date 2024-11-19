import csv
import os


class DataHandler:
    # 拥有爬取githubRank数据
    def __init__(self, folder_name='../data', file_name='github_rank.csv'):
        self.folder_name = folder_name
        self.file_name = file_name
        self.file_path = os.path.join(self.folder_name, self.file_name)
        self._ensure_folder_exists()
        self._initialize_csv()

    def _ensure_folder_exists(self):
        # 创建文件夹
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"已创建文件夹: {self.folder_name}")

    def _initialize_csv(self):
        # 写入表头
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['login', 'name', 'location', 'created_at', 'followers', 'repositories'])
            print(f"已创建 CSV 文件并写入表头: {self.file_path}")

    def write_user_data(self, user_data):
        """
        将用户数据写入 CSV 文件。

        :param user_data: 字典，包含用户信息
        """
        with open(self.file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                user_data.get('login', 'N/A'),
                user_data.get('name', 'N/A'),
                user_data.get('location', 'N/A'),
                user_data.get('created_at', 'N/A'),
                user_data.get('followers', 0),
                user_data.get('repositories', 0)
            ])
        print(f"已写入用户数据: {user_data.get('login', 'N/A')}")
