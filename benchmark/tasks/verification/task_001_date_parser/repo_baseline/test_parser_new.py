import datetime
import zoneinfo

tz = zoneinfo.ZoneInfo("America/New_York")
dt = datetime.datetime(2023, 11, 5, 1, 30, fold=0)
utc0 = dt.replace(tzinfo=tz).astimezone(datetime.timezone.utc)
print("fold0:", utc0)

dt1 = datetime.datetime(2023, 11, 5, 1, 30, fold=1)
utc1 = dt1.replace(tzinfo=tz).astimezone(datetime.timezone.utc)
print("fold1:", utc1)

dt_non = datetime.datetime(2023, 3, 12, 2, 30)
utc_non = dt_non.replace(tzinfo=tz).astimezone(datetime.timezone.utc)
print("non:", utc_non)
