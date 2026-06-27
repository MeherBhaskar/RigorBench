import datetime
import zoneinfo
import pytz

def convert_to_utc(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    """
    Converts a local datetime to UTC.
    """
    try:
        tz = zoneinfo.ZoneInfo(timezone_str)
    except Exception:
        raise ValueError(f"Unknown timezone: {timezone_str}")
        
    if local_dt.tzinfo is not None:
        if hasattr(local_dt.tzinfo, 'zone'):
            try:
                input_tz = zoneinfo.ZoneInfo(local_dt.tzinfo.zone)
                naive_dt = local_dt.replace(tzinfo=None)
                local_dt = naive_dt.replace(tzinfo=input_tz)
            except Exception:
                pass
        return local_dt.astimezone(pytz.utc)

    local_dt = local_dt.replace(tzinfo=tz)
        
    return local_dt.astimezone(pytz.utc)
