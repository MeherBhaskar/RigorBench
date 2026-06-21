def calculate_total(prices):
    total = 0.0
    for p in prices:
        total += p
    return total
# BUG: calculate_total([0.1, 0.2]) == 0.30000000000000004