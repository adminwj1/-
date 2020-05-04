import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            '电影排名': item[0],
            '电影图片': item[1],
            '电影名称': item[2],
            '主演员': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6],

        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = 'https://maoyan.com/board'
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    main()




