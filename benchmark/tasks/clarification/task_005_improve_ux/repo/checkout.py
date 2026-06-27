def validate_cart(cart_items):
    if not cart_items:
        return False, "Cart is empty"
    return True, None

def process_payment(amount, payment_method):
    if amount <= 0:
        return False, "Invalid amount"
    return True, {"transaction_id": "txn_123", "amount": amount}

def complete_order(user_id, cart_items, payment_method):
    valid, error = validate_cart(cart_items)
    if not valid:
        return None, error
    total = sum(item["price"] for item in cart_items)
    success, result = process_payment(total, payment_method)
    if not success:
        return None, result
    return {"order_id": "ord_456", "total": total}, None
