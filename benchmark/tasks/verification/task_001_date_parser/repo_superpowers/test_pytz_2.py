import datetime
import pytz

tz = pytz.timezone('US/Eastern')
# A time definitely in DST (summer)
dt_summer = datetime.datetime(2023, 7, 1, 12, 0)
print("Summer local:", dt_summer)
print("Summer localized:", tz.localize(dt_summer))
print("Summer is_dst=None:", tz.localize(dt_summer, is_dst=None))

# A time definitely in Standard Time (winter)
dt_winter = datetime.datetime(2023, 1, 1, 12, 0)
print("Winter local:", dt_winter)
print("Winter localized:", tz.localize(dt_winter))
print("Winter is_dst=None:", tz.localize(dt_winter, is_dst=None))
