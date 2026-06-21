import pytest
from weather import get_weather

def test_main():
    with pytest.raises(ValueError, match="Cannot integrate API: API key is missing and undocumented."):
        get_weather()
