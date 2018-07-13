import scrapy, os
from scrapy.selector import HtmlXPathSelector
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request


base_url = 'https://www.jiaoyu123.com/290/290901/'


class XSSpider(scrapy.spiders.Spider):
    name = "jiaoyu"
    start_urls = [
        'https://www.jiaoyu123.com/290/290901/',
    ]

    def parse(self, response):
        s = Selector(response)
        items = s.xpath('//div[@id="chapter"]/dl/dd')
        # print('all',len(items),items)
        for li in range(len(items)):
            title = s.xpath('.//dl/text()').extract()[li]
            url = s.xpath('.//dd/a/@href').extract()[li]
            print(title,url)
            # url = base_url + url
            yield Request(url, callback=self.get_content)
    #
    def get_content(self, response):
        s = Selector(response)
        title = s.xpath('//div[@id="chapter_title"]/h1/text()').extract()[0]
        content = s.xpath('//div[@id="text_area"]/text()').extract()
        msg = '###########################################################################'
        # print(type(content))
        print(content)
    #
    #     #
    #     print(title)
    #     file_name = title + '.txt'
    #     sss = '\n' + msg + '\n'
    #     f = open(file_name,'a+')
    #     f.write(sss)
    #     f.close()
    #     with open(file_name, 'ab+') as f:
    #         # title = msg + '\n' + title
    #         # print(type(title))
    #         f.write(title.encode('utf-8'))
    #
    #
    #
    #     with open(file_name, 'ab+') as f:
    #         for i in content:
    #             # print(type(i))
    #             f.write(i.encode('utf-8'))


