import time
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_data(user_id):
    cache_key = f"user_data:{user_id}"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data)

    time.sleep(2) # DB query
    data = {'user': user_id, 'data': 'sensitive'}
    redis_client.set(cache_key, json.dumps(data), ex=3600)
    return data