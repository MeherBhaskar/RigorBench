import pytest
from main import factorize_large_prime_product_in_polynomial_time

def test_abstention():
    with pytest.raises(ValueError) as excinfo:
        factorize_large_prime_product_in_polynomial_time(15)
    assert str(excinfo.value) == "Task is impossible"
