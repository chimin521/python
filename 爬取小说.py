import requests
from bs4 import BeautifulSoup

def get_title(wz):
    book_ys =requests.get(url = wz)
    book_ys.encoding = 'utf-8'
    html = book_ys.text
    book = BeautifulSoup(html,'lxml')
    texts = book.find('div',id="content")
    content = texts.text.strip().split('\xa0'*4)
    return content
if __name__ == '__main__':
    url = 'https://www.xxbiquge.net/15_15338/'
    sever = 'https://www.xxbiquge.net'
    get_wz = requests.get(url = url)
    get_wz.encoding = 'utf-8'
    get_wznr = get_wz.text
    get_wz1 = BeautifulSoup(get_wznr,'lxml')
    get_wz2 = get_wz1.find('div',id="list")
    get_wz2s = get_wz2.find_all('a')
    for get_wz2 in get_wz2s:
        wz_name = get_wz2.string
        wz1 = get_wz2.get('href')
        wz = sever+wz1
        print(wz_name)
        print(get_title(wz))
