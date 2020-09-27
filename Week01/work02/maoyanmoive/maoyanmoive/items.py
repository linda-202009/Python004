# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MaoyanmoiveItem(scrapy.Item):
    moiveNames = scrapy.Field()
    moiveTypes = scrapy.Field()
    moiveUpdates = scrapy.Field()