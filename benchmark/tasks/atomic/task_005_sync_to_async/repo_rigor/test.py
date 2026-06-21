import asyncio
from api import user_route

def test_main():
    result = asyncio.run(user_route())
    assert result == {'id': 1}
