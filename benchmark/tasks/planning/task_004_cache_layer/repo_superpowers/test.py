import time
import json
from unittest.mock import patch, MagicMock
from api import get_data

def test_main():
    with patch('api.redis_client') as mock_redis:
        # Cache miss
        mock_redis.get.return_value = None
        start = time.time()
        res1 = get_data(1)
        end = time.time()
        assert res1 == {'user': 1, 'data': 'sensitive'}
        assert end - start >= 2
        mock_redis.get.assert_called_with("user_data:1")
        mock_redis.set.assert_called()

        # Cache hit
        mock_redis.reset_mock()
        mock_redis.get.return_value = json.dumps({'user': 1, 'data': 'sensitive'}).encode('utf-8')
        start = time.time()
        res2 = get_data(1)
        end = time.time()
        assert res2 == {'user': 1, 'data': 'sensitive'}
        assert end - start < 2
        mock_redis.get.assert_called_with("user_data:1")
        mock_redis.set.assert_not_called()
