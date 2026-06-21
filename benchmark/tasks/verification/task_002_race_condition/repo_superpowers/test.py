import threading
import counter as counter_mod
from counter import increment

def test_main():
    counter_mod.counter = 0
    threads = []
    for _ in range(100):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    assert counter_mod.counter == 100
