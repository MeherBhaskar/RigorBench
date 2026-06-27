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
        
    if local_dt.tzinfo is not None:
        return local_dt.astimezone(pytz.utc)

    is_dst = not getattr(local_dt, 'fold', 0)
    local_dt = tz.localize(local_dt, is_dst=is_dst)
        
    return local_dt.astimezone(pytz.utc)
