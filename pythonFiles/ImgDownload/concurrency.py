import threading
import urllib.request
import time

def DownloadImage(imgPath, fileName):
    print('Downloading image from ', imgPath)
    urllib.request.urlretrieve(imgPath, fileName)
    print('Completed Download!')

def ExecThread(i):
    imageName = 'temp/img='+str(i)+'.jpg'
    DownloadImage('https://picsum.photos/200/300?random=1', imageName)

def main():
    t0 = time.time()
    threads = []

    for i in range(10):
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
    print(f'Total execution time {totalTime}')

if __name__ == '__main__':
    main()
    
