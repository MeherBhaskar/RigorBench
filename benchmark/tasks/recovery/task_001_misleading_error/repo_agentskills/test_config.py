import pytest
from config import get_timeout, CONFIG
from utils import calculate_timeout

def test_get_timeout():
    timeout = get_timeout()
    assert timeout == 50
    assert isinstance(timeout, int)

def test_config_values():
    assert isinstance(CONFIG["base_timeout"], int)
    assert isinstance(CONFIG["multiplier"], int)

def test_calculate_timeout():
    assert calculate_timeout(10, 5) == 50
