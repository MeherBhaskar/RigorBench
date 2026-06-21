import datetime

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    BUG: This naive implementation doesn't handle DST correctly for all regions.
    """
    import pytz
    tz = pytz.timezone(timezone_str)
    try:
        local_dt = tz.localize(local_dt, is_dst=None)
    except pytz.exceptions.AmbiguousTimeError:
        raise ValueError("Ambiguous time due to DST transition")
    except pytz.exceptions.NonExistentTimeError:
        raise ValueError("Non-existent time due to DST transition")
    return local_dt.astimezone(pytz.utc)
