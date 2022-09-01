import random
import threading
import time

# Variável que será manipulada ao mesmo tempo pelas threads
counter = 1

# Este código mostra um exemplo em que duas threads estao acessando a mesma
# variável global. Para isso foram criadas duas threads, WorkerA e WorkerB, 
# ambas são responsáveis por manipular a variável global counter incrementando e decrementando
# seu valor em 1 unidade.

def WorkerA():
    # Define a variável counter como global
    global counter
    while counter < 10:
        counter += 1
        print(f'Worker A is incrementing counter to {counter}')
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)

def WorkerB():
    # Define a variável counter como global
    global counter
    while counter > -10:
        counter -= 1
        print(f'Worker B is decrementing counter to {counter}')
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)

def main():
    t0 = time.time()

    # Realiza a criação das duas threads que irão manipular o valor de counter
    thread1 = threading.Thread(target=WorkerA)
    thread2 = threading.Thread(target=WorkerB)

    # Coloca as threads em modo de espera
    thread1.start()
    thread2.start()

    # Executa a thread
    thread1.join()
    thread2.join()

    # Calcula tempo de execução
    t1 = time.time()

    print(f'Execution Time {t1-t0}')

if __name__ == '__main__':
    main()