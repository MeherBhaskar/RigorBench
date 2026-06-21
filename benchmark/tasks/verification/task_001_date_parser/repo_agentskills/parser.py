import datetime

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    """
    import pytz
    from pytz.exceptions import UnknownTimeZoneError, AmbiguousTimeError, NonExistentTimeError
    
    try:
        tz = pytz.timezone(timezone_str)
    except UnknownTimeZoneError:
        raise ValueError(f"Unknown timezone: {timezone_str}")
        
    try:
        local_dt = tz.localize(local_dt, is_dst=None)
    except (AmbiguousTimeError, NonExistentTimeError) as e:
        raise ValueError(f"Invalid or ambiguous time: {e}")
        
    return local_dt.astimezone(pytz.utc)
