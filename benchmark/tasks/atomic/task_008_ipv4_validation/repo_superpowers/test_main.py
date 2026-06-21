import pytest
from main import is_valid_ipv4

def test_is_valid_ipv4():
    assert is_valid_ipv4('192.168.1.1') is True
    assert is_valid_ipv4('255.255.255.255') is True
    assert is_valid_ipv4('0.0.0.0') is True
    assert is_valid_ipv4('256.1.1.1') is False
    assert is_valid_ipv4('192.168.1') is False
    assert is_valid_ipv4('192.168.1.1.1') is False
    assert is_valid_ipv4('192.168.01.1') is False
    assert is_valid_ipv4('abc.def.ghi.jkl') is False
    assert is_valid_ipv4('') is False
    assert is_valid_ipv4('1..1.1') is False
    assert is_valid_ipv4('-1.0.0.0') is False
