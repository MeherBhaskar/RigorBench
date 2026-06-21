import time
import json
import pytest
from unittest.mock import patch
import api

def test_main():
    with patch('api.r') as mock_redis:
        # First call: cache miss
        mock_redis.get.return_value = None
        
        start_time = time.time()
        res1 = api.get_data(1)
        duration1 = time.time() - start_time
        
        assert duration1 >= 2
        assert res1 == {'user': 1, 'data': 'sensitive'}
        mock_redis.set.assert_called_once_with('user_data:1', json.dumps({'user': 1, 'data': 'sensitive'}))
        
        # Second call: cache hit
        mock_redis.get.return_value = json.dumps({'user': 1, 'data': 'sensitive'})
        
        start_time = time.time()
        res2 = api.get_data(1)
        duration2 = time.time() - start_time
        
        assert duration2 < 1
        assert res2 == {'user': 1, 'data': 'sensitive'}
