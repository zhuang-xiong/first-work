# 开发时间： 2022/4/13 16:57
# 开发者 ：zhuang-xiong
import urllib.request
import urllib.parse
from lxml import etree
import requests
'''
最终结果：爬出来结果250个名字
'''
'''
post请求
'''
'''
去掉ssl问题
'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/79.0.3945.88 Safari/537.36',
            'Cookie': ''
          }
s = requests.session()
s.keep_alive = False
def get_url(url):
    r = requests.get(url,headers = headers,timeout=30)
    # r.raise_for_status()
    # r.encoding = r.apparent_encoding

    return r.text
def get_content(html):
    tree = etree.HTML(html)
    attr = tree.xpath("//*[@class='hd']//*[@class ='title'][1]")
    '''
    返回值是列表，没有text方法
    '''
    for i in attr:
        print(i.text)
for i in range(0,11):
    html = get_url("https://movie.douban.com/top250?start="+(str)(25*i))
    # print(html)
    text = get_content(html)
print(text)

