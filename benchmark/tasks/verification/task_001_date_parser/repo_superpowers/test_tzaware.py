import datetime
import pytz

tz = pytz.timezone('US/Eastern')
dt = datetime.datetime.now(pytz.utc)
try:
    loc = tz.localize(dt)
except Exception as e:
    print("Error:", type(e), e)

