import threading
import counter

def test_main():
    counter.counter = 0
    threads = []
    for _ in range(100):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    assert counter.counter == 100
