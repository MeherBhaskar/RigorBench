import pytest
import time
from main import execute_with_recovery, TransientError, FatalError

def test_success_first_try(monkeypatch):
    sleeps = []
    monkeypatch.setattr(time, 'sleep', lambda d: sleeps.append(d))
    
    def action():
        return 'success'
        
    result = execute_with_recovery(action)
    assert result == 'success'
    assert len(sleeps) == 0

def test_transient_recovery(monkeypatch):
    sleeps = []
    monkeypatch.setattr(time, 'sleep', lambda d: sleeps.append(d))
    
    attempts = 0
    def action():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise TransientError('transient')
        return 'success'
        
    result = execute_with_recovery(action)
    assert result == 'success'
    assert attempts == 3
    assert sleeps == [1.0, 2.0]

def test_transient_exhaustion(monkeypatch):
    sleeps = []
    monkeypatch.setattr(time, 'sleep', lambda d: sleeps.append(d))
    
    attempts = 0
    def action():
        nonlocal attempts
        attempts += 1
        raise TransientError('transient')
        
    with pytest.raises(TransientError):
        execute_with_recovery(action, max_retries=2, base_delay=0.1)
        
    assert attempts == 3
    assert sleeps == [0.1, 0.2]

def test_fatal_error(monkeypatch):
    sleeps = []
    monkeypatch.setattr(time, 'sleep', lambda d: sleeps.append(d))
    
    attempts = 0
    def action():
        nonlocal attempts
        attempts += 1
        raise FatalError('fatal')
        
    with pytest.raises(FatalError):
        execute_with_recovery(action)
        
    assert attempts == 1
    assert len(sleeps) == 0
