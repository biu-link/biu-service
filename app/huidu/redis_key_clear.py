from util.redis_db import RedisDB
import json

config = {
    'host': '47.103.22.21',
    'port': 6379,
    'password': 'trs.8899',
    'database': 0
}
redis = RedisDB(config)

values = redis.keys('uploadApk:*')
# values = redis.keys('abc')
for key in values:
    print(key)
    redis.expire(key, 6000)
