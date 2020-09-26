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
import pandas as pd
import xlwt

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
    for Num in range(5):
        movieType += selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[%s]/text()' %(Num))

    mylist = (movieName[0], movieType[::], movieDate[0])
    return mylist

def saveExcel(mylist, maoyanUrl):
    moiveName = "Week01_Work01_Moive"
    save_file = pd.DataFrame(mylist)
    title = "爬取猫眼地址: %s" %(maoyanUrl)
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                        num_format_str='#,##0.00')
    style1 = xlwt.easyxf('align: wrap on, vert centre, horiz left', 
                        num_format_str='YYYY-MM-D')

    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('电影TOP10列表', cell_overwrite_ok = True)

    ws.write(0, 0, title, style0) 
    ws.write(1, 0, "制表人: Linda", style1)
    ws.write(2, 0, "电影名称", style0)
    ws.write(2, 1, "电影类型", style0)
    ws.write(2, 2, "上映日期", style0)
    num = 2
    for i in mylist:
        num += 1
        ws.write(num, 0, i[0])
        ws.write(num, 1, i[1])
        ws.write(num, 2, i[2])

    wb.save('./Week01/%s.csv' %(moiveName))


def main():
    maoYanUrl = "https://maoyan.com/films?showType=3"
    topUrl = getURL(maoYanUrl)
    print ("-" * 120)
    Mylist = [getDetailPage(i) for i in topUrl]
    saveExcel(mylist=Mylist, maoyanUrl=maoYanUrl)
        
if __name__ == "__main__":
    main()



