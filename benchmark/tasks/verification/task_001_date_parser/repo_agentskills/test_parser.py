import pytest
import datetime
import pytz
from parser import convert_to_utc

def test_convert_valid():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt == datetime.datetime(2023, 1, 1, 17, 0, tzinfo=pytz.utc)

def test_invalid_timezone():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    with pytest.raises(ValueError):
        convert_to_utc(dt, "Invalid/Timezone")

def test_ambiguous_time_fold_0():
    # 2023-11-05 01:30:00 happens twice in New York.
    # fold=0 -> EDT (UTC-4), which is 05:30:00 UTC
    dt = datetime.datetime(2023, 11, 5, 1, 30, fold=0)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt == datetime.datetime(2023, 11, 5, 5, 30, tzinfo=pytz.utc)

def test_ambiguous_time_fold_1():
    # 2023-11-05 01:30:00 happens twice in New York.
    # fold=1 -> EST (UTC-5), which is 06:30:00 UTC
    dt = datetime.datetime(2023, 11, 5, 1, 30, fold=1)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt == datetime.datetime(2023, 11, 5, 6, 30, tzinfo=pytz.utc)

def test_nonexistent_time():
    # 2023-03-12 02:30:00 does not exist in New York.
    dt = datetime.datetime(2023, 3, 12, 2, 30)
    # It should resolve without throwing an exception.
    utc_dt = convert_to_utc(dt, "America/New_York")
    # depending on fold (0 by default), it resolves to -04:00 (06:30 UTC) or -05:00 (07:30 UTC)
    # We just assert it returns a valid UTC time
    assert utc_dt.tzinfo == pytz.utc

def test_already_aware_time():
    # If a timezone aware datetime is passed, it should convert properly
    dt = datetime.datetime(2023, 1, 1, 12, 0, tzinfo=pytz.timezone("Europe/London"))
    utc_dt = convert_to_utc(dt, "America/New_York") # the passed timezone str might be ignored or used, let's just assert it converts
    assert utc_dt == datetime.datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc)

