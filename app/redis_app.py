# -*- coding:utf-8 -*-

from util.redis_db import RedisDB
import json

code = 'system_config_public_html_service'
value = RedisDB().get(code)
print(value)

if value:
    print(json.loads(value).get('content'))

content = '''
'''

value = {"title": "隐私政策", "content": content}
# RedisDB().set(code, json.dumps(value, ensure_ascii=False))

value = RedisDB().get(code)
print(value)
