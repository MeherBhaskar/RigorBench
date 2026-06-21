from decimal import Decimal

def calculate_total(prices):
    total = Decimal('0.0')
    for p in prices:
        total += Decimal(str(p))
    return float(total)
# BUG: calculate_total([0.1, 0.2]) == 0.30000000000000004