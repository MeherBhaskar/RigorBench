def is_valid_ipv4(ip: str) -> bool:
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            num = int(part)
            if not (0 <= num <= 255):
                return False
            if str(num) != part:
                return False
        except ValueError:
            return False
    return True
