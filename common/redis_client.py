import redis


class RedisClient(object):
    """redis数据库操作工具"""

    _instance = None

    def __init__(self, host, port, db, pwd, expire=120):
        if pwd:
            self.r = redis.Redis(host, port, db, pwd)
        else:
            self.r = redis.Redis(host, port, db)
        self.redis_expire = expire

    def init_app(self, app):
        setattr(app, 'redis_client', self)

    def string_set(self, key, value, expire=None):
        """写入键值对"""

        # 判断是否有过期时间，没有就设置默认值
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = self.redis_expire
        self.r.set(key, value, ex=expire_in_seconds)

    def string_get(self, key):
        """读取键值对内容"""

        value = self.r.get(key)
        return value.decode('utf-8') if value else value

    def hash_set(self, name, key, value):
        """写入hash表"""

        self.r.hset(name, key, value)

    def hash_get(self, name, key):
        """读取指定hash表的键值"""

        value = self.r.hget(name, key)
        return value.decode('utf-8') if value else value

    def hash_set_keys(self, key, *value):
        """读取指定hash表的所有给定字段的值"""

        value = self.r.hmset(key, *value)
        return value

    def hash_get_keys(self, name):
        """获取指定hash表所有的值"""

        return self.r.hgetall(name)

    def delete(self, *names):
        """删除一个或者多个"""

        self.r.delete(*names)

    def hash_del(self, name, key):
        """删除指定hash表的键值"""

        self.r.hdel(name, key)

    def expire(self, name, expire=None):
        """设置过期时间"""

        expire_in_seconds = expire or self.redis_expire
        self.r.expire(name, expire_in_seconds)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
