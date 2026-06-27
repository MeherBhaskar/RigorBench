def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item.get("quantity", 1)
    return total

def apply_discount(total, discount_code):
    discounts = {"SAVE10": 0.10, "SAVE20": 0.20}
    rate = discounts.get(discount_code, 0)
    return total * (1 - rate)
