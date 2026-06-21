import datetime

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    """
    from zoneinfo import ZoneInfo
    tz = ZoneInfo(timezone_str)
    
    if local_dt.tzinfo is None:
        local_dt = local_dt.replace(tzinfo=tz)
    else:
        local_dt = local_dt.astimezone(tz)
        
    return local_dt.astimezone(datetime.timezone.utc)
