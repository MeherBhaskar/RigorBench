from zoneinfo import ZoneInfo
import datetime

def convert_to_utc_zoneinfo(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    tz = ZoneInfo(timezone_str)
    if local_dt.tzinfo is None:
        local_dt = local_dt.replace(tzinfo=tz)
    return local_dt.astimezone(datetime.timezone.utc)

print(convert_to_utc_zoneinfo(datetime.datetime(2023, 11, 5, 1, 30), 'US/Eastern'))
