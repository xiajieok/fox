import scrapy
import os
import urllib
from scrapy.selector import Selector
from scrapy.http import Request
from fox.items import ReadItem

base_url = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/'


class ReadSpider(scrapy.spiders.Spider):
    name = "read"
    start_urls = [
        'http://python3-cookbook.readthedocs.io/zh_CN/latest/',
    ]
    allowed_domains = ['python3-cookbook.readthedocs.io']

    def parse(self, response):
        item = ReadItem()
        s = Selector(response)
        items = s.xpath('//div[@class="wy-menu wy-menu-vertical"]/ul/li')
        for li in range(len(items)):
            chapter_url = s.xpath('.//a/@href').extract()[li]
            chapter_url = base_url + chapter_url
            if "chapters" in chapter_url:
                # print(chapter_url)
                item['chapter_url'] = chapter_url
                yield Request(item['chapter_url'], callback=self.get_lessons, meta={'item': item})

    def get_lessons(self, response):
        print('------------------获取 节------------------')
        item = response.meta['item']
        s = Selector(response)
        items = s.xpath('//li[@class="toctree-l2"]')
        # print(items)
        for li in range(len(items)):
            lesson_url = s.xpath('.//a/@href').extract()[li][3:]
            if "c0" in lesson_url:
                lesson_url = base_url + lesson_url
                print('节 的URL', lesson_url)
                item['lesson_url'] = lesson_url
                yield Request(item['lesson_url'], callback=self.get_content, meta={'item': item})
            else:
                print('NO')

    def get_content(self, response):
        print('------------------获取 内容------------------')
        item = response.meta['item']
        content = response.xpath('//div[@class="section"]').extract()[0]
        title = response.xpath('//div[@class="section"]/h1/text()').extract()[0]
        # print('我是获取的内容', content.strip('\n'))
        print('我是获取的内容', title)
        try:
            item['title'] = title
            item['content'] = content
        except Exception as e:
            print(e)
        return item
