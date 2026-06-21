import datetime
import pytz

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    """
    try:
        tz = pytz.timezone(timezone_str)
    except pytz.exceptions.UnknownTimeZoneError:
        raise ValueError(f"Unknown timezone: {timezone_str}")
        
    try:
        local_dt = tz.localize(local_dt, is_dst=None)
    except pytz.exceptions.AmbiguousTimeError:
        raise ValueError("Ambiguous time")
    except pytz.exceptions.NonExistentTimeError:
        raise ValueError("Non-existent time")
        
    return local_dt.astimezone(pytz.utc)
