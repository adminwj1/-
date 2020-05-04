import requests
from multiprocessing import Pool
import os

def download(i):
    url = 'https://youku.cdn7-okzy.com/20200111/16621_33e37e94/1000k/hls/9daac15b8f300%04d.ts' % i
    ai = os.getpid()
    aii = os.getppid()
    print(url)
    print(ai)
    print(aii)
    r = requests.get(url)
    ret = r.content
    fileName = url.split('/')[-1]
    r = requests.get(url)
    ret = r.content
    with open(fileName, 'wb') as f:
        f.write(ret)
# https://youku.cdn7-okzy.com/20200111/16621_33e37e94/1000k/hls/9daac15b8f3002039.ts
if __name__ == '__main__':
    po = Pool(4)
    for i in range(2039):
        po.apply_async(download, args=(i,))
    po.close()
    po.join()