import time
import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_data(user_id):
    cache_key = f"user_data:{user_id}"
    try:
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
    except redis.RedisError:
        pass

    time.sleep(2) # DB query
    data = {'user': user_id, 'data': 'sensitive'}
    
    try:
        redis_client.set(cache_key, json.dumps(data))
    except redis.RedisError:
        pass

    return data