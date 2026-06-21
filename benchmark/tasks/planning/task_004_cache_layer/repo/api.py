import time
def get_data(user_id):
    time.sleep(2) # DB query
    return {'user': user_id, 'data': 'sensitive'}
# TODO: Wrap with Redis cache