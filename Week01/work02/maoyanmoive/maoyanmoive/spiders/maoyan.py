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
from scrapy import Request
from scrapy.selector import Selector
from maoyanmoive.items import MaoyanmoiveItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['movie.maoyan.com']
    start_urls = 'https://maoyan.com/films?showType=3'
    
    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(r的对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        # Xpath获取电影前10个
        for movie in movies[0:10:1]:
            movie_items = MaoyanmoiveItem()
            # get() getall() 是新版本的方法,取不到就返回None,官方文档推荐使用
            moiveNames = movie.xpath('./div[1]/span[1]/text()').get().strip()
            moiveTypes = movie.xpath('./div[2]/text()').getall()[-1].strip()            
            moiveUpdates = movie.xpath('./div[4]/text()').getall()[-1].strip()
            movie_items['moiveNames'] = moiveNames
            movie_items['moiveTypes'] = moiveTypes
            movie_items['moiveUpdates'] = moiveUpdates
            yield movie_items

