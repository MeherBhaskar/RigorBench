import pytest
from unittest.mock import patch, mock_open
from loader import load_config

def test_load_config_success():
    m = mock_open(read_data='{"key": "value"}')
    with patch('builtins.open', m):
        result = load_config()
        assert result == '{"key": "value"}'

def test_load_config_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_config()
