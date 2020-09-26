# -*- coding: utf-8 -*-
# Author: Linda
# Date: 2020-09-23
# Desc: 
'''
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址： https://maoyan.com/films?showType=3
要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
'''

import scrapy
from lxml import etree
from scrapy import Request
from scrapy.selector import Selector
from maoyanmoive.items import MaoyanmoiveItem

class MaoYanMoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    
    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(r的对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    def parse(self, r):
        html = etree.HTML(r.text, etree.HTMLParser())
        moiveName = html.xpath('//dd/div[1]/div[2]/a/div/div[1]/span[1]/text()')
        moiveType = html.xpath('//dd/div[1]/div[2]/a/div/div[2]/text()')
        moiveUpdate = html.xpath('//dd/div[1]/div[2]/a/div/div[4]/text()')

        moiveTypes = eval(str(moiveType).replace(' ', '').replace('\\n', ''))
        moiveUpdates = eval(str(moiveUpdate).replace(' ', '').replace('\\n', ''))

        for i in moiveTypes:
            if len(i) == 0:
                moiveTypes.remove(i)
                moiveUpdates.remove(i)

        movieLists = list(zip(moiveName, moiveTypes, moiveUpdates))
        movieList10 = movieLists[0:10:1]

        movieData = [ MaoyanmoiveItem(moiveNames=i[0], moiveTypes=i[1], moiveUpdates=i[2]) for i in movieList10]
        
        return movieData

