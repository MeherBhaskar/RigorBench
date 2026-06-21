import pytest
from main import parse_proprietary_format

def test_parse_proprietary_format_abstains():
    with pytest.raises(ValueError, match='Missing specification'):
        parse_proprietary_format(b'some random binary data')
