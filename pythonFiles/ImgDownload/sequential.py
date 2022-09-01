import urllib.request
import time

def DownloadImage(imgPath, fileName):
    print('Downloading image from ', imgPath)
    # Método para fazer o download e salvar o arquivo no imgPath
    urllib.request.urlretrieve(imgPath, fileName)

def main():
    # Faz o download de 10 imagens sequencialmente
    for i in range(10):
        imageName = 'temp/img='+str(i)+'.jpg'
        DownloadImage('https://picsum.photos/200/300?random=1', imageName)

if __name__ == '__main__':
    t1 = time.time()
    main()
    print('Spend Time: ', time.time()-t1)


