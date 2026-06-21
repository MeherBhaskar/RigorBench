import datetime
import pytz
from parser import convert_to_utc

# Test 1: Normal time
try:
    dt1 = datetime.datetime(2020, 1, 1, 12, 0)
    print("Normal:", convert_to_utc(dt1, "US/Eastern"))
except Exception as e:
    print("Normal error:", repr(e))

# Test 2: Ambiguous time (Fall back)
try:
    dt2 = datetime.datetime(2020, 11, 1, 1, 30)
    print("Ambiguous:", convert_to_utc(dt2, "US/Eastern"))
except Exception as e:
    print("Ambiguous error:", repr(e))

# Test 3: Non-existent time (Spring forward)
try:
    dt3 = datetime.datetime(2020, 3, 8, 2, 30)
    print("Non-existent:", convert_to_utc(dt3, "US/Eastern"))
except Exception as e:
    print("Non-existent error:", repr(e))
