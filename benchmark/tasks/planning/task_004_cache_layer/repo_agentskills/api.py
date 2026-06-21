import time
import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_data(user_id):
    cache_key = f"user:{user_id}"
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return json.loads(cached_result)

    time.sleep(2) # DB query
    result = {'user': user_id, 'data': 'sensitive'}
    
    redis_client.set(cache_key, json.dumps(result))
    return result