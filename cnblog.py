# 开发时间： 2022/4/16 19:46
# 开发者 ：zhuang-xiong
from lxml import etree
import requests
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/79.0.3945.88 Safari/537.36',
            'Cookie': ''
          }
s = requests.session()
s.keep_alive = False
def get_url(url):
    r = requests.get(url,headers = headers,timeout=30)
    return r.text

def get_content(html):
    tree = etree.HTML(html)
    # attr = tree.xpath("//*@[class = 'content']//*[target='_blank']")
    attr = tree.xpath("//*[@class='news_entry']//*[@target='_blank']")

    for i in attr:
        print(i.text)
# def write_to_csv(filename):
#     with open(filename,'w',encoding='utf-8') as f:
#         filednames=['条数','标题']
#         csv_writer = csv.writer(f)
#         csv_writer.writerow(filednames)
#         '''
#         写入表头
#         '''
#         for i in range(0,301):
#             csv_writer.writerow(i,text)




for i in range(0,11):
    html = get_url('https://news.cnblogs.com/n/page/'+(str)(i))
    text = get_content(html)
    # write_to_csv('title.csv')
print(text)