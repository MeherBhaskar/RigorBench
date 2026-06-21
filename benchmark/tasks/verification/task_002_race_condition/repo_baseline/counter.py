import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    with lock:
        temp = counter
        counter = temp + 1
# TODO: Fix race condition when 100 threads call increment()