import pytest
from main import with_recovery, sleep_delays

def test_recovery_success():
    sleep_delays.clear()
    attempts = 0

    @with_recovery(max_retries=3, base_delay=1)
    def flaky_function():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError('Failed')
        return 'Success'

    assert flaky_function() == 'Success'
    assert attempts == 3
    assert sleep_delays == [1, 2]

def test_recovery_failure():
    sleep_delays.clear()
    attempts = 0

    @with_recovery(max_retries=2, base_delay=2)
    def failing_function():
        nonlocal attempts
        attempts += 1
        raise ConnectionError('Always fails')

    with pytest.raises(ConnectionError):
        failing_function()
    assert attempts == 3
    assert sleep_delays == [2, 4]
