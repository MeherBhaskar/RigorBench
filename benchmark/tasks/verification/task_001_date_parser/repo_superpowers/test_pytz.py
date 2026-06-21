import datetime
import pytz

tz = pytz.timezone('US/Eastern')
local_dt = datetime.datetime(2023, 11, 5, 1, 30) # ambiguous, fallback
try:
    print(tz.localize(local_dt))
except Exception as e:
    print("Error 1:", type(e), e)

local_dt_2 = datetime.datetime(2023, 3, 12, 2, 30) # nonexistent, spring forward
try:
    print(tz.localize(local_dt_2))
except Exception as e:
    print("Error 2:", type(e), e)

