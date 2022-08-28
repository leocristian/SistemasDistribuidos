import random
import threading
import time

counter = 1

def WorkerA():
    global counter
    while counter < 10:
        counter += 1
        print(f'Worker A is incrementing counter to {counter}')
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)

def WorkerB():
    global counter
    while counter > -10:
        counter -= 1
        print(f'Worker B is decrementing counter to {counter}')
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)

def main():
    t0 = time.time()
    thread1 = threading.Thread(target=WorkerA)
    thread2 = threading.Thread(target=WorkerB)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time()

    print(f'Execution Time {t1-t0}')

if __name__ == '__main__':
    main()