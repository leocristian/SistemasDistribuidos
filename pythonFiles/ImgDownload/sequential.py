import urllib.request
import time

def DownloadImage(imgPath, fileName):
    print('Downloading image from ', imgPath)
    urllib.request.urlretrieve(imgPath, fileName)

def main():
    for i in range(10):
        imageName = 'temp/img='+str(i)+'.jpg'
        DownloadImage('https://picsum.photos/200/300?random=1', imageName)

if __name__ == '__main__':
    t1 = time.time()
    main()
    print('Spend Time: ', time.time()-t1)


