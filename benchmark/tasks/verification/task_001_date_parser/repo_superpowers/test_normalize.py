import datetime
import pytz

tz = pytz.timezone('US/Eastern')

# Nonexistent time (spring forward, 2:30 AM)
dt1 = datetime.datetime(2023, 3, 12, 2, 30)
try:
    loc1 = tz.localize(dt1)
    norm1 = tz.normalize(loc1)
    print("Nonexistent localized:", loc1)
    print("Nonexistent normalized:", norm1)
except Exception as e:
    print("Nonexistent error:", type(e), e)

# Ambiguous time (fallback, 1:30 AM)
dt2 = datetime.datetime(2023, 11, 5, 1, 30)
try:
    loc2 = tz.localize(dt2)
    norm2 = tz.normalize(loc2)
    print("Ambiguous localized:", loc2)
    print("Ambiguous normalized:", norm2)
except Exception as e:
    print("Ambiguous error:", type(e), e)

