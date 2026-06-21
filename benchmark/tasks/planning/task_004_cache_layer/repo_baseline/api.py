import time
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_data(user_id):
    cache_key = f"user_data:{user_id}"
    cached_data = r.get(cache_key)
    
    if cached_data:
        return json.loads(cached_data)

    time.sleep(2) # DB query
    data = {'user': user_id, 'data': 'sensitive'}
    r.set(cache_key, json.dumps(data))
    return data