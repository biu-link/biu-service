# -*- coding:utf-8 -*-

from util.redis_db import RedisDB

config = {
    'host': 'r-uf6sok3p4wuz8ywvi6pd.redis.rds.aliyuncs.com',
    'port': 6379,
    'password': 'codeflag2021&',

    # 39:测试环境    40:生产环境
    'database': 40
}
redis = RedisDB(config)

code = 'wechat_access_token_aiqgb'
value = redis.get(code)
print(value)

config['database'] = 39
redis = RedisDB(config)
print(redis.get(code))

redis.set(code, value)
value = redis.get(code)
print(value)

