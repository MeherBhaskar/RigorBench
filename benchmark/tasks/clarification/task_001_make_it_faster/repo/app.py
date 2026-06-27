import time

def process_request(data):
    # Simulate some processing
    time.sleep(0.1)
    return {"result": data, "processed": True}

def batch_process(items):
    results = []
    for item in items:
        results.append(process_request(item))
    return results
