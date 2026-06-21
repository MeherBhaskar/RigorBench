import asyncio
from api import user_route

def test_main():
    res = asyncio.run(user_route())
    assert res == {'id': 1}
