import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
}
for i in range(12):
    url = 'https://youku.cdn7-okzy.com/20200111/16621_33e37e94/1000k/hls/9daac15b8f300%04d.ts' % i
    print(url)
    fileName = url.split('/')[-1]
    r = requests.get(url, headers=headers)
    ret = r.content
    with open(fileName, 'wb') as f:
        print('正在下载')
        f.write(ret)