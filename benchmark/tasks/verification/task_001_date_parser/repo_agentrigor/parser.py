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
                tz_name = local_dt.tzinfo.zone
                zi = zoneinfo.ZoneInfo(tz_name)
                current_offset = local_dt.utcoffset()
                naive = local_dt.replace(tzinfo=None)
                offset0 = naive.replace(tzinfo=zi, fold=0).utcoffset()
                offset1 = naive.replace(tzinfo=zi, fold=1).utcoffset()
                if current_offset not in (offset0, offset1):
                    # It's using the incorrect LMT offset from pytz.timezone construction.
                    # We override it with standard zoneinfo.
                    local_dt = naive.replace(tzinfo=zi)
            except Exception:
                pass
        return local_dt.astimezone(pytz.utc)

    # replace tzinfo with the given timezone. This properly uses local_dt.fold
    local_dt = local_dt.replace(tzinfo=tz)
        
    return local_dt.astimezone(pytz.utc)
