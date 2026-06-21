from db import get_user
async def user_route():
    return await get_user(1)
# TODO: make get_user async, update route to await it