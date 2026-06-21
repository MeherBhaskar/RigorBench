import pytest
from unittest.mock import patch
from main import fetch_with_recovery

def test_fetch_success_first_try():
    def fetch():
        return 'success'
    assert fetch_with_recovery(fetch) == 'success'

@patch('time.sleep')
def test_fetch_success_after_retries(mock_sleep):
    attempts = 0
    def fetch():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError('Failed')
        return 'success'
    assert fetch_with_recovery(fetch) == 'success'
    assert mock_sleep.call_count == 2
    mock_sleep.assert_any_call(0.1)
    mock_sleep.assert_any_call(0.2)

@patch('time.sleep')
def test_fetch_fails_after_max_retries(mock_sleep):
    def fetch():
        raise ConnectionError('Failed')
    with pytest.raises(ConnectionError):
        fetch_with_recovery(fetch, max_retries=2, base_delay=0.1)
    assert mock_sleep.call_count == 2
    mock_sleep.assert_any_call(0.1)
    mock_sleep.assert_any_call(0.2)
