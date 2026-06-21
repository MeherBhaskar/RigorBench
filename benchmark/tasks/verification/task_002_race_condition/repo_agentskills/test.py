import threading
from counter import increment
import counter

def test_main():
    counter.counter = 0
    threads = []
    for _ in range(100):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    assert counter.counter == 100
