import scrapy
from scrapy.selector import HtmlXPathSelector

class PigSpider(scrapy.spiders.Spider):
    name = "dog"
    '''
    app name
    '''

    start_urls = [
        'http://www.xiaohuar.com/hua/',
    ]

    def parse(self,respone):
        current_url = respone.url
        body = respone.body
        unicode_boy = respone.body_as_unicode()
        from scrapy.selector import Selector
        url_list = Selector(response=respone).xpath('//a/@href')
        # print(url_list)
        for url in url_list:
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)