# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#
# class FoxItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     url = scrapy.Field()
#     # school = scrapy.Field()
#
#     price = scrapy.Field()
#     title = scrapy.Field()
#     site = scrapy.Field()
#     floor = scrapy.Field()
#     style = scrapy.Field()
#     share = scrapy.Field()
#     size = scrapy.Field()
class ReadItem(scrapy.Item):
    chapter_url = scrapy.Field()
    lesson_url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()