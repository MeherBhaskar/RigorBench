import datetime
import pytz

def convert_to_utc_test(local_dt: datetime.datetime, timezone_str: str) -> datetime.datetime:
    tz = pytz.timezone(timezone_str)
    if local_dt.tzinfo is not None:
        # Already aware, so we normalize it just in case? Or just convert?
        return local_dt.astimezone(pytz.utc)
    # The bug could be here:
    local_dt = tz.localize(local_dt, is_dst=None)
    return local_dt.astimezone(pytz.utc)

dt = datetime.datetime.now(pytz.utc)
print(convert_to_utc_test(dt, 'US/Eastern'))
