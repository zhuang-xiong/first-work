# 开发时间： 2022/4/12 14:06
# 开发者 ：zhuang-xiong
'''
bs4适合简单的爬虫，整体爬取
'''
import requests
from bs4 import BeautifulSoup
import csv
import json
def post_url(url):
    try:
        r = requests.post(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('成功访问！')
        return r.text
    except:
        print("访问出错！")
        return " "
def get_url(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('成功访问！')
        return r.text
    except:
        print("访问出错！")
        return " "
#
# def get_content(html):
#     final = []
#     bs = BeautifulSoup(html,'html.parser')
#     body = bs.body
#     data = body.find_all('div',{'class':'content'})
#     text = body.find_all('p',{'class':"Wonderful--title--23U6SgE"})
#     for i in text:
#         print(i.get_text())
# html = get_url("https://www.tmall.com/")
# print(get_content(html))
# print(post_url("https://movie.douban.com/top250"))
# print('****************************************')
print(get_url("https://www.youtube.com/"))