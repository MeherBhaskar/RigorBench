def process_items(items):
    doubled = [i*2 for i in items]
    return list(map(str, doubled))