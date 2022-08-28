import time
import random

def CalculatePrimeFactors(n):
    primFac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primFac.append(d)
            n //= d
        d += 1
    if n > 1:
        primFac.append(n)
    return primFac

def main():
    t0 = time.time()
    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(CalculatePrimeFactors(rand))
    t1 = time.time()
    totalTime = t1 - t0

    print(f'Execution Time: {totalTime}')

if __name__ == '__main__':
    main()