import pytest
from unittest.mock import patch, call
from main import fetch_with_recovery, NetworkError, RateLimitError, MaxRetriesExceededError

@patch('main.time.sleep')
@patch('main.mock_api_call')
def test_successful_call(mock_api, mock_sleep):
    mock_api.return_value = 'success'
    result = fetch_with_recovery('http://test.com')
    assert result == 'success'
    mock_api.assert_called_once_with('http://test.com')
    mock_sleep.assert_not_called()

@patch('main.time.sleep')
@patch('main.mock_api_call')
def test_recovers_after_network_error(mock_api, mock_sleep):
    mock_api.side_effect = [NetworkError(), NetworkError(), 'success']
    result = fetch_with_recovery('http://test.com', max_retries=3)
    assert result == 'success'
    assert mock_api.call_count == 3
    mock_sleep.assert_has_calls([call(1), call(2)])

@patch('main.time.sleep')
@patch('main.mock_api_call')
def test_recovers_after_rate_limit_error(mock_api, mock_sleep):
    mock_api.side_effect = [RateLimitError(), 'success']
    result = fetch_with_recovery('http://test.com')
    assert result == 'success'
    assert mock_api.call_count == 2
    mock_sleep.assert_called_once_with(1)

@patch('main.time.sleep')
@patch('main.mock_api_call')
def test_max_retries_exceeded(mock_api, mock_sleep):
    mock_api.side_effect = NetworkError()
    with pytest.raises(MaxRetriesExceededError):
        fetch_with_recovery('http://test.com', max_retries=2)
    assert mock_api.call_count == 3
    mock_sleep.assert_has_calls([call(1), call(2)])

@patch('main.time.sleep')
@patch('main.mock_api_call')
def test_mixed_errors(mock_api, mock_sleep):
    mock_api.side_effect = [NetworkError(), RateLimitError(), 'success']
    result = fetch_with_recovery('http://test.com', max_retries=3)
    assert result == 'success'
    assert mock_api.call_count == 3
    mock_sleep.assert_has_calls([call(1), call(2)])
