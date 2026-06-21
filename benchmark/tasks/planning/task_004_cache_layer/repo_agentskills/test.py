import time
from unittest.mock import patch, MagicMock
from api import get_data
import json

@patch('api.redis_client')
def test_main(mock_redis):
    # Setup mock
    mock_redis.get.return_value = None
    
    # First call (cache miss)
    start = time.time()
    result1 = get_data(1)
    duration1 = time.time() - start
    assert result1 == {'user': 1, 'data': 'sensitive'}
    assert duration1 >= 2.0
    mock_redis.set.assert_called_with('user:1', json.dumps(result1))
    
    # Second call (cache hit)
    mock_redis.get.return_value = json.dumps(result1)
    start = time.time()
    result2 = get_data(1)
    duration2 = time.time() - start
    assert result2 == {'user': 1, 'data': 'sensitive'}
    assert duration2 < 1.0 # Should be fast
