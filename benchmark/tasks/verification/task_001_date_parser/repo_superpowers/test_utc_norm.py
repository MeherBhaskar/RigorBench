import datetime
import pytz

tz = pytz.timezone('US/Eastern')
dt = datetime.datetime(2023, 3, 12, 2, 30)

loc = tz.localize(dt)
utc1 = loc.astimezone(pytz.utc)

norm = tz.normalize(loc)
utc2 = norm.astimezone(pytz.utc)

print("UTC without normalize:", utc1)
print("UTC with normalize:", utc2)
