import pytest
from main import calculate_total_price

def test_calculate_total_price_abstains():
    with pytest.raises(ValueError, match='Missing price information'):
        calculate_total_price(['apple', 'banana'])
