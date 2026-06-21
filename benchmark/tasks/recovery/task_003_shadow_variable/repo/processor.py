def process_items(items):
    list = [i*2 for i in items] # BUG: shadows builtin
    return list(map(str, list)) # Throws TypeError