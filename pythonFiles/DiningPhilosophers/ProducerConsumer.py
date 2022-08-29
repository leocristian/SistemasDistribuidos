import random
import threading
import time

class Producer(threading.Thread):
    def __init__(self, integer, condition):
        threading.Thread.__init__(self)
        self.integers = integer
        self.condition = condition

    def run(self):
        for x in range(10):
            integer = x
            self.condition.acquire()
            print(f'condition acquired by {self.name}')
            self.integers.append(integer)
            print(f'{integer} appended to list by {self.name}')
            print(f'condition notified by {self.name}')
            self.condition.notify()
            print(f'condition released by {self.name}')
            self.condition.release()
            time.sleep(10)

class Consumer(threading.Thread):
    def __init__(self, integer, condition):
        threading.Thread.__init__(self)
        self.integers = integer
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            print(f'condition acquired by {self.name}')
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print(f'{integer} popped from list by {self.name}')
                    break
                print(f'condition wait by {self.name}')
                self.condition.wait()
            print(f'condition released by {self.name}')
            self.condition.release()

def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()