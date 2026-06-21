import threading
counter = 0
def increment():
    global counter
    temp = counter
    counter = temp + 1
# TODO: Fix race condition when 100 threads call increment()