import time
import random
from multiprocessing import Process

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

def ExecuteProc(): # Função que será executada pelo processo
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(CalculatePrimeFactors(rand))

def main():
    print('Starting number crunching')
    t0 = time.time()
    procs = []
    for i in range(10):
        # Instancia um novo processo responsável por executar apenas uma função
        proc = Process(target=ExecuteProc, args=())
        procs.append(proc)
        # Coloca o processo em modo de espera
        proc.start()

        # executa todos os processos instanciados anteriormente
    for proc in procs:
        proc.join()
    t1 = time.time()
    totalTime = t1 - t0

    print(f'Execution Time: {totalTime}')

if __name__ == '__main__':
    main()