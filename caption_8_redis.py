#
#   driver: pip install redis
#   server: brew install redis
#

import redis

r=redis.Redis(host='localhost',port=6379,db=0)
r.set("foo",'hello world')
print(r.get("foo"))