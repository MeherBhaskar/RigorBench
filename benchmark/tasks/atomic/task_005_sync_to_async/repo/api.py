from db import get_user
def user_route():
    return get_user(1)
# TODO: make get_user async, update route to await it