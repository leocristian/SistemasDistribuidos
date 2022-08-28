import threading

l1 = threading.Lock()
l1.acquire()
l1.acquire()

print('hello')