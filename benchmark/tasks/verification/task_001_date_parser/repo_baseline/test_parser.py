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

def test_nonexistent_time_exact_values():
    # 2023-03-12 02:30:00 does not exist in New York.
    # fold=0 should resolve to the pre-transition offset (EST: UTC-5), which is 07:30:00 UTC
    dt_fold0 = datetime.datetime(2023, 3, 12, 2, 30, fold=0)
    utc_dt0 = convert_to_utc(dt_fold0, "America/New_York")
    assert utc_dt0 == datetime.datetime(2023, 3, 12, 7, 30, tzinfo=pytz.utc)

    # fold=1 should resolve to the post-transition offset (EDT: UTC-4), which is 06:30:00 UTC
    dt_fold1 = datetime.datetime(2023, 3, 12, 2, 30, fold=1)
    utc_dt1 = convert_to_utc(dt_fold1, "America/New_York")
    assert utc_dt1 == datetime.datetime(2023, 3, 12, 6, 30, tzinfo=pytz.utc)

def test_lord_howe_ambiguous_time():
    # Lord Howe Island DST transition has a 30-minute offset change.
    # On 2023-04-02, standard time ends/starts, and 01:45:00 occurs twice:
    # fold=0 -> Daylight saving (UTC+11:00) -> 01:45 - 11 hours = 2023-04-01 14:45 UTC
    # fold=1 -> Standard time (UTC+10:30) -> 01:45 - 10h 30m = 2023-04-01 15:15 UTC
    dt0 = datetime.datetime(2023, 4, 2, 1, 45, fold=0)
    utc0 = convert_to_utc(dt0, "Australia/Lord_Howe")
    assert utc0 == datetime.datetime(2023, 4, 1, 14, 45, tzinfo=pytz.utc)

    dt1 = datetime.datetime(2023, 4, 2, 1, 45, fold=1)
    utc1 = convert_to_utc(dt1, "Australia/Lord_Howe")
    assert utc1 == datetime.datetime(2023, 4, 1, 15, 15, tzinfo=pytz.utc)

def test_zoneinfo_aware_input():
    import zoneinfo
    # Pass a datetime already aware with standard ZoneInfo
    tz = zoneinfo.ZoneInfo("Europe/Paris")
    # Paris on 2023-06-01 is CEST (UTC+2)
    dt = datetime.datetime(2023, 6, 1, 12, 0, tzinfo=tz)
    utc_dt = convert_to_utc(dt, "America/New_York")
    # 12:00 UTC+2 is 10:00 UTC
    assert utc_dt == datetime.datetime(2023, 6, 1, 10, 0, tzinfo=pytz.utc)
