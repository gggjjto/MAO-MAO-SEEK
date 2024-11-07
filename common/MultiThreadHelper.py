import concurrent.futures
import threading

import requests


class MultiThreadHelper:
    # 多线程工具类
    def __init__(self, max_workers=5):
        """
        初始化多线程工具类
        :param max_workers: 最大线程数，默认是 5
        """
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers)
        self.lock = threading.Lock()  # 线程锁用于避免打印或共享资源冲突

    def submit_task(self, func, *args, **kwargs):
        """
        提交一个任务到线程池中
        :param func: 要执行的函数
        :param args: 传递给函数的位置参数
        :param kwargs: 传递给函数的关键字参数
        :return: future 对象
        """
        return self.executor.submit(func, *args, **kwargs)

    def wait_for_all(self, futures):
        """
        等待所有任务完成
        :param futures: future 对象列表
        :return: 所有任务的结果列表
        """
        results = []
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f"Generated an exception: {exc}")
        return results

    def shutdown(self):
        """
        关闭线程池
        """
        self.executor.shutdown(wait=True)


# 示例使用
if __name__ == "__main__":
    # 示例函数：模拟从一个 URL 获取数据
    def fetch_url(url):
        response = requests.get(url)
        return {"url": url, "status_code": response.status_code}


    # 线程帮助类实例化
    multi_thread_helper = MultiThreadHelper(max_workers=10)

    # 要获取的 URL 列表
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.openai.com",
        "https://www.stackoverflow.com"
    ]

    # 提交所有任务
    futures = [multi_thread_helper.submit_task(fetch_url, url) for url in urls]

    # 等待所有任务完成，并获取结果
    results = multi_thread_helper.wait_for_all(futures)

    # 打印结果
    for result in results:
        print(f"URL: {result['url']}, Status Code: {result['status_code']}")

    # 关闭线程池
    multi_thread_helper.shutdown()
