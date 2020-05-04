#encoding: utf-8
'''
cookie的格式：
Set-Cookie: NAME=VALUE: EXPIRES/MNax-age=DATE: Path=PATH: Domain=DOMAIN_NAME: SECURE
NAME：cookie的名字
VALUE：cookie的值
Expires：cookie的过期时间
Path：cookie作用的路径
Domain：cookie作用的域名
SECURE：是否只在HTTPS写一下起作用

'''
# from urllib import request
import requests
# 使用cookielib库和HTTPCookieProcessor模拟登录：
# 1、不适用cookie去请求人人网的个人主页
url = "https://www.zhihu.com/"
# cookie = '''q_c1=e9f1f2d11d624a0e8dd2c3e2dbae5596|1582564680000|1582564680000; _zap=36e59380-492a-48e7-9e48-cf4895ff5803; d_c0="ALCZqtIg3hCPTh4TXufWUju8lTCbpubyH7A=|1582564679"; _ga=GA1.2.1980558573.1582625096; tst=r; q_c1=fb3b24c4861346ec9885beac6f101883|1582792585000|1582792585000; __utma=51854390.1980558573.1582625096.1582970701.1582970701.1; __utmz=51854390.1582970701.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20180102=1^3=entry_date=20180102=1; _gid=GA1.2.1095017678.1585033785; _xsrf=1253e601-7b19-4c88-b18e-04d9cb5568f8; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584804679,1585033784,1585059501,1585062444; capsion_ticket="2|1:0|10:1585062445|14:capsion_ticket|44:M2QxMTAxNDQyOTU5NGRlY2E2YTRiZTAyYzhiYjg3NWU=|7f802b9a5c5e64c0dd9b2493045bb464fce185b905488818380a3f83924722d9"; z_c0="2|1:0|10:1585062455|4:z_c0|92:Mi4xY0pzaUJ3QUFBQUFBc0ptcTBpRGVFQ1lBQUFCZ0FsVk5OM0JuWHdCblR0alBTWi1tWllvYWlha3VybG1PYWNhMGJB|37a422e11601ed9fc21839a5fd88997f06ffc20c3b2b7d1d04a5dc99c42b579d"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585062468; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1585062762|1585059501'''
headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
cookie ={
    'cookie':'q_c1=e9f1f2d11d624a0e8dd2c3e2dbae5596|1582564680000|1582564680000; _zap=36e59380-492a-48e7-9e48-cf4895ff5803; d_c0="ALCZqtIg3hCPTh4TXufWUju8lTCbpubyH7A=|1582564679"; _ga=GA1.2.1980558573.1582625096; tst=r; q_c1=fb3b24c4861346ec9885beac6f101883|1582792585000|1582792585000; __utma=51854390.1980558573.1582625096.1582970701.1582970701.1; __utmz=51854390.1582970701.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20180102=1^3=entry_date=20180102=1; _gid=GA1.2.1095017678.1585033785; _xsrf=1253e601-7b19-4c88-b18e-04d9cb5568f8; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584804679,1585033784,1585059501,1585062444; capsion_ticket="2|1:0|10:1585062445|14:capsion_ticket|44:M2QxMTAxNDQyOTU5NGRlY2E2YTRiZTAyYzhiYjg3NWU=|7f802b9a5c5e64c0dd9b2493045bb464fce185b905488818380a3f83924722d9"; z_c0="2|1:0|10:1585062455|4:z_c0|92:Mi4xY0pzaUJ3QUFBQUFBc0ptcTBpRGVFQ1lBQUFCZ0FsVk5OM0JuWHdCblR0alBTWi1tWllvYWlha3VybG1PYWNhMGJB|37a422e11601ed9fc21839a5fd88997f06ffc20c3b2b7d1d04a5dc99c42b579d"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585062468; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1585062762|1585059501'
}
req = requests.get(url, headers=headers, cookies=cookie)
resp = req.text
# print(req.text).decode('utf-8')
# print(resp.read().decode('utf-8'))
with open('renren.html','w',encoding='utf8') as f:
    '''
    write函数必须写一个str的数据类型
    resp.read()读出来的是一个bytes数据类型
    bytes ---> decode(解码) --->str
    str ---> encode(编码) ---> bytes
    '''
    f.write(resp)