import scrapy, os
from scrapy.selector import Selector
from scrapy.http import Request
from fox import items as ReadItem

base_url = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/'


class ReadSpider(scrapy.spiders.Spider):
    name = "read"
    start_urls = [
        'http://python3-cookbook.readthedocs.io/zh_CN/latest/',
    ]

    def parse(self, response):
        links = []
        s = Selector(response)
        items = s.xpath('//li[@class="toctree-l2"]/a')
        #循环出所有的章节URL
        for i in range(len(items)):
            url = s.xpath('//li[@class="toctree-l2"]/a/@href').extract()[i]
            #取出href
            if 'c0' in url or 'c1' in url:
                #排除其他无关URL
                c_url = base_url + url
                #拼接
                links.append(c_url)
            else:
                print('no', url)
        for link in links:
            print(link)
            yield Request(link, callback=self.get_content)

    def get_content(self, response):
        #根据URL,获取内容
        print('#########################获取HTML#########################')
        item = ReadItem.ReadItem()
        content = response.xpath('//div[@class="section"]').extract()[0]
        item['content'] = content
        item['url'] = response.url
        yield item
