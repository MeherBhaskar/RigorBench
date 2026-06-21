import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        temp = counter
        counter = temp + 1