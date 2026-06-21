def calculate_timeout(base_timeout, multiplier):
    # This will fail if multiplier is a string, but the traceback will point here
    return base_timeout * multiplier
