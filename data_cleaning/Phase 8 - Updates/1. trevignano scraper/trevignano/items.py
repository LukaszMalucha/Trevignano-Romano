# -*- coding: utf-8 -*-


import scrapy


class TrevignanoItem(scrapy.Item):
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
