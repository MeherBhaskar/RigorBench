import pytest
import time
from main import execute_with_retry, TransientError, FatalError, MaxRetriesExceededError

def test_success_first_try(mocker):
    mock_func = mocker.Mock(return_value='success')
    mock_sleep = mocker.patch('time.sleep')
    result = execute_with_retry(mock_func, 3, 1, 10)
    assert result == 'success'
    assert mock_func.call_count == 1
    mock_sleep.assert_not_called()

def test_retry_transient_error(mocker):
    mock_func = mocker.Mock(side_effect=[TransientError(), TransientError(), 'success'])
    mock_sleep = mocker.patch('time.sleep')
    result = execute_with_retry(mock_func, 3, 1, 10)
    assert result == 'success'
    assert mock_func.call_count == 3
    mock_sleep.assert_has_calls([mocker.call(1), mocker.call(2)])

def test_fatal_error(mocker):
    mock_func = mocker.Mock(side_effect=[TransientError(), FatalError()])
    mock_sleep = mocker.patch('time.sleep')
    with pytest.raises(FatalError):
        execute_with_retry(mock_func, 3, 1, 10)
    assert mock_func.call_count == 2
    mock_sleep.assert_called_once_with(1)

def test_max_retries_exceeded(mocker):
    mock_func = mocker.Mock(side_effect=TransientError())
    mock_sleep = mocker.patch('time.sleep')
    with pytest.raises(MaxRetriesExceededError):
        execute_with_retry(mock_func, 2, 1, 10)
    assert mock_func.call_count == 3
    mock_sleep.assert_has_calls([mocker.call(1), mocker.call(2)])

def test_max_delay(mocker):
    mock_func = mocker.Mock(side_effect=[TransientError()] * 4 + ['success'])
    mock_sleep = mocker.patch('time.sleep')
    result = execute_with_retry(mock_func, 5, 1, 5)
    assert result == 'success'
    assert mock_func.call_count == 5
    mock_sleep.assert_has_calls([mocker.call(1), mocker.call(2), mocker.call(4), mocker.call(5)])
