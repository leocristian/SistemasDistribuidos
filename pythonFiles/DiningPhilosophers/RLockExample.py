import threading
import time

def test(lock):
    lock.acquire()
    print(threading.current_thread())
    time.sleep(1)
    # what would happen if the the comment on line 9 is removed?
    # lock.release() 

l1 = threading.RLock()

t1 = threading.Thread(target=test, args=(l1,))
t2 = threading.Thread(target=test, args=(l1,))

t1.start()
t1.join()
t2.start()
t2.join()

print('Hello')