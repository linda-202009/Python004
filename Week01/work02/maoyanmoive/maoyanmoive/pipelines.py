# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import xlwt
import pandas as pd
import json

class MaoyanmoivePipeline:

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, movie_items, spider):
        moiveNames = movie_items['moiveNames']
        moiveTypes = movie_items['moiveTypes']
        moiveUpdates = movie_items['moiveUpdates']

        fileone = f'{moiveNames},{moiveTypes},{moiveUpdates}\n'
        with open('./maoyanmovie_top10.csv', 'a+', encoding='utf-8') as article:
            article.write(fileone)

        return movie_items






