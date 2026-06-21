import datetime

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    BUG: This naive implementation doesn't handle DST correctly for all regions.
    """
    import pytz
    tz = pytz.timezone(timezone_str)
    
    try:
        # is_dst=None raises an exception for ambiguous or non-existent times
        local_dt = tz.localize(local_dt, is_dst=None)
    except pytz.AmbiguousTimeError as e:
        raise ValueError(f"Ambiguous local time: {e}") from e
    except pytz.NonExistentTimeError as e:
        raise ValueError(f"Non-existent local time: {e}") from e
        
    return local_dt.astimezone(pytz.utc)
