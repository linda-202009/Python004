# -*- coding:utf-8 -*-
# Author: Linda
# Date: 2020-09-23
# Desc: 
'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中.
猫眼电影网址： https://maoyan.com/films?showType=3
'''

import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import re

def getURL(maoyanUrl):
    headers = {"Content-Type": "text/html; charset=utf-8",
            'Accept': '*/*;',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

    body = ""

    r = requests.get(url=maoyanUrl, headers=headers, data=body)

    # 是否被反爬
    print ("\033[1;35m 访问链接: %s \033[0m" %(r.url ))
    print ("\033[94m 正常链接: %s \033[0m" %(maoyanUrl))
    if r.url != maoyanUrl:
        print ("\033[93m *** 提示: 恭喜哦，被反爬虫了，需要点击上面访问链接，打开链接，重新访问认证即可 *** \033[0m")

    r.close()
    bsr = bs(r.text, 'html.parser')
    selector = lxml.etree.HTML(r.text)

    movie_list = []

    for bsObj in bsr.find_all('div', attrs={'class': "movie-item-hover"}, limit=10):
        for Obj in bsObj.find_all('a'):
            Dlink = str(maoyanUrl.split('?')[0].split('/films')[0].strip())+str(Obj.get('href').strip())
            movie_list.append(Dlink)
    return movie_list

def getDetailPage(dateilUrl):
    headers = {"Content-Type": "text/html; charset=utf-8",
            'Accept': '*/*;',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

    body = ""

    r2 = requests.get(url=dateilUrl, headers=headers, data=body)

    selector = lxml.etree.HTML(r2.text)

    # 电影名称
    movieName = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()') 

    # 上映日期
    movieDate = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')

    # 电影类型
    movieType = []
    for i in range(5):
        movieType += selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[%s]/text()' %(i))

    mylist = (dateilUrl, movieName[0], movieDate[0], movieType[::])
    print (mylist)

def main():
    URL = getURL("https://maoyan.com/films?showType=3")
    print ("-" * 120)
    [getDetailPage(i) for i in URL]
        
if __name__ == "__main__":
    main()



