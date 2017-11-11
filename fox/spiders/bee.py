import scrapy,os
from scrapy.selector import HtmlXPathSelector
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request
from fox import items as fox_items
class PigSpider(scrapy.spiders.Spider):
    name = "bee"
    '''
    app name
    '''

    start_urls = [
        'http://www.xiaohuar.com/hua/',
    ]

    def parse(self,response):
        # current_url = respone.url
        # body = respone.body
        # unicode_boy = respone.body_as_unicode()
        # print(body)
        hxs = HtmlXPathSelector(response)
        items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
        # items = Selector(response=)('//div[@class="item_list infinite_scroll"]/div')
        for i in range(len(items)):
            src = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
            name = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            school = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            if name and src and school:

                try:
                    print('执行item')
                    item = fox_items.FoxItem()
                    item['name'] = name[0] + '.jpg'
                    item['src'] =  src[0]
                    item['school'] = school[0]
                    print(item)
                    yield item

                    # request.urlretrieve(ab_src,file_path)
                except Exception as e:
                    print(e)
            # 获取所有的url，继续访问，并在其中寻找相同的url
            # all_urls = hxs.select('//a/@href').extract()
            # for url in all_urls:
            #     if url.startswith('http://www.xiaohuar.com/list-1-'):
            #         # print(url)
            #         yield Request(url, callback=self.parse)



























