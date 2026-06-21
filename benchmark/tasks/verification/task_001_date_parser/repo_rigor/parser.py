import datetime

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    BUG: This naive implementation doesn't handle DST correctly for all regions.
    """
    import pytz
    tz = pytz.timezone(timezone_str)
    
    if local_dt.tzinfo is None:
        local_dt = tz.localize(local_dt, is_dst=None)
    
    return local_dt.astimezone(pytz.utc)
