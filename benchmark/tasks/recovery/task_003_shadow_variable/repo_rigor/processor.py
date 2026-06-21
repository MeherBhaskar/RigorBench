def process_items(items):
    lst = [i*2 for i in items]
    return list(map(str, lst))