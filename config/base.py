from datetime import timedelta

##################################################################################
DEBUG = True
LOG_LEVEL = 'DEBUG'
LOG_PATH = '/srv/services/templates/logs/x.log'


####################################################################################
# database


def gen_sql_uri(db_name, charset='utf8mb4'):
    driver = 'mysql+pymysql'
    user_pwd = 'user:passwd'
    host_port = 'localhost:3306'
    return f'{driver}://{user_pwd}@{host_port}/{db_name}?charset={charset}'


SQLALCHEMY_DATABASE_URI = gen_sql_uri('db1')

SQLALCHEMY_BINDS = {
    'db2': gen_sql_uri('db2'),
    'db3': gen_sql_uri('db3')
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_recycle': 50,
    'pool_size': 5,
    'max_overflow': -1
}

####################################################################################
# token 密钥
JWT_SECRET_KEY = 'aHi9cqDOWaS8zJFFT/55MQ=='
# token 失效时间
TOKEN_EXP_DELTA = timedelta(days=30)

####################################################################################
# redis 数据库连接参数

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
# 第几个 redis 数据库
REDIS_DB = 10
# 如果没有密码，就写 None
REDIS_PWD = None
# 过期时间: seconds
REDIS_EXPIRE = 300

########################################################################################
# 接口返回数据 JSON 格式

JSON_AS_ASCII = False
RESTFUL_JSON = dict(ensure_ascii=False)
