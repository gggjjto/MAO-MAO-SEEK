import json

import redis


class RedisTool(object):
    # Redis工具类
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        """
        初始化 Redis 连接。

        :param host: Redis 服务器地址，默认为 'localhost'
        :param port: Redis 服务器端口，默认为 6379
        :param db: Redis 数据库编号，默认为 0
        :param password: 连接 Redis 的密码，默认为 None
        """
        # 创建一个 Redis 连接实例
        self.r = redis.StrictRedis(host=host, port=port, db=db, password=password)

    def set_value(self, key, value):
        """
        设置指定键的值。

        :param key: 键
        :param value: 值
        :return: 设置操作的结果（True 表示成功，False 表示失败）
        """
        return self.r.set(key, value)

    def get_value(self, key):
        """
        获取指定键的值。

        :param key: 键
        :return: 键对应的值，如果键不存在则返回 None
        """
        a = self.r.get(key)
        if a is None:
            return a
        return a.decode('utf-8')

    def del_key(self, key):
        """
        删除指定的键。

        :param key: 键
        :return: 删除操作的结果（被删除的键的数量）
        """
        return self.r.delete(key)

    def set_hash_kv(self, name, key, value):
        """
        设置哈希表中的键值对。

        :param name: 哈希表名称
        :param key: 键
        :param value: 值
        :return: 设置操作的结果（1 表示新键被设置，0 表示键已存在并被覆盖）
        """
        return self.r.hset(name, key, value)

    def get_all_hash_kv(self, name):
        """
        获取哈希表中的所有键值对。

        :param name: 哈希表名称
        :return: 哈希表中的所有键值对（字典格式）
        """
        return self.r.hgetall(name)

    def get_hash_kv(self, name, key):
        """
        获取哈希表中指定键的值。

        :param name: 哈希表名称
        :param key: 键
        :return: 指定键的值，如果键不存在则返回 None
        """
        return self.r.hget(name, key)

    def del_hash_kv(self, name, *keys):
        """
        删除哈希表中的一个或多个键。

        :param name: 哈希表名称
        :param keys: 要删除的键，可以传入多个键
        :return: 删除操作的结果（被删除的键的数量）
        """
        return self.r.hdel(name, *keys)

    def set_json(self, key, json_obj):
        """
        将一个 JSON 对象存储为字符串。

        :param key: 键
        :param json_obj: 要存储的 JSON 对象（字典或列表）
        :return: 设置操作的结果（True 表示成功，False 表示失败）
        """
        # 将 JSON 对象转换为字符串
        json_str = json.dumps(json_obj)
        # 将 JSON 字符串存储到 Redis 中
        return self.r.set(key, json_str)

    def get_json(self, key):
        """
        获取存储为 JSON 字符串的对象，并将其解析为 JSON 对象。

        :param key: 键
        :return: 解析后的 JSON 对象（字典或列表），如果键不存在则返回 None
        """
        # 从 Redis 中获取存储的 JSON 字符串
        json_bytes = self.r.get(key)
        if json_bytes:
            # 将 JSON 字符串解析为 Python 对象
            return json.loads(json_bytes)
        return None


# 创建 RedisTool 实例
redis_tool = RedisTool()
