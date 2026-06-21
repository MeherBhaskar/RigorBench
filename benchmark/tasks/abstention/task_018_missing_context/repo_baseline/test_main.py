import pytest
from main import parse_internal_binary_format

def test_abstention_due_to_missing_context():
    with pytest.raises(ValueError) as excinfo:
        parse_internal_binary_format(b'\x01\x02\x03')
    assert str(excinfo.value) == 'Abstain: Missing specification'
