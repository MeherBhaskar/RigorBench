import asyncio
from api import user_route

def test_main():
    assert asyncio.run(user_route()) == {'id': 1}
