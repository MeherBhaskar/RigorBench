import pytest
import datetime
from parser import convert_to_utc

def test_normal_time():
    # A normal time that exists and is unambiguous
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "US/Eastern")
    assert utc_dt.hour == 17  # UTC is 5 hours ahead of EST in January

def test_non_existent_time():
    # Spring forward in US/Eastern: 2:30 AM does not exist on 2023-03-12
    dt = datetime.datetime(2023, 3, 12, 2, 30)
    with pytest.raises(ValueError, match="Non-existent local time"):
        convert_to_utc(dt, "US/Eastern")

def test_ambiguous_time():
    # Fall back in US/Eastern: 1:30 AM happens twice on 2023-11-05
    dt = datetime.datetime(2023, 11, 5, 1, 30)
    with pytest.raises(ValueError, match="Ambiguous local time"):
        convert_to_utc(dt, "US/Eastern")
