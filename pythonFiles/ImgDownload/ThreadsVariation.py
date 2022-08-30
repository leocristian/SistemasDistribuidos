import threading
import urllib.request
import time
import matplotlib.pyplot

def DownloadImage(imgPath, fileName):
    # print('Downloading image from ', imgPath)
    urllib.request.urlretrieve(imgPath, fileName)
    # print('Completed Download!')

def ExecThread(i):
    imageName = 'temp/img='+str(i)+'.jpg'
    DownloadImage('https://picsum.photos/200/300?random=1', imageName)

def main():
    nOfThreads = 10
    execTimes = []
    nOfThreadsArr = []

    for i in range(10):

        t0 = time.time()
        threads = []

        for i in range(nOfThreads):
            # Realiza a criação de uma nova thread responsável por executar o método atribuido em target
            thread = threading.Thread(target=ExecThread, args=(i,))
            threads.append(thread)
            # Inicializa a thread em modo de espera
            thread.start()
        # Executa todas as threads que estavam em modo de espera
        for i in threads:
            i.join()

        t1 = time.time()
        totalTime = t1-t0
        execTimes.append(totalTime)
        nOfThreadsArr.append(nOfThreads)

        print(f'Number of Threads: {nOfThreads}\nTotal execution time {totalTime}')

        nOfThreads += 10

    matplotlib.pyplot.plot(nOfThreadsArr, execTimes)
    matplotlib.pyplot.xlabel('Number of threads')
    matplotlib.pyplot.ylabel('Time (ms)')
    matplotlib.pyplot.show()

if __name__ == '__main__':
    main()
    
