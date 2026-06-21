from unittest import mock
import fakeredis
from api import get_data

def test_main():
    fake_redis = fakeredis.FakeRedis()
    
    with mock.patch('api.redis_client', fake_redis):
        with mock.patch('api.time.sleep') as mock_sleep:
            # First call, cache miss, should hit DB (sleep)
            result1 = get_data(1)
            assert result1 == {'user': 1, 'data': 'sensitive'}
            mock_sleep.assert_called_once_with(2)
            
            mock_sleep.reset_mock()
            
            # Second call, cache hit, should not hit DB (no sleep)
            result2 = get_data(1)
            assert result2 == {'user': 1, 'data': 'sensitive'}
            mock_sleep.assert_not_called()
