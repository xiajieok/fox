import scrapy, os
from scrapy.selector import HtmlXPathSelector
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request

opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


class DuowanSpider(scrapy.spiders.Spider):
    name = "duowan"
    start_urls = [
        'http://tu.duowan.com/m/bxgif',
    ]

    def parse(self, response):
        s = Selector(response)
        items = s.xpath('body/div[@id="layout"]/div[@id="content"]/div[@class="i-list"]/ul[@id="pic-list"]/li')
        for li in range(len(items)):
            # name = s.xpath('.//li[@class="box"]/em/a/text()').extract()[li]
            img_url = s.xpath('.//li[@class="box"]/a/@href').extract()[li]
            img_url = img_url.replace('gallery', 'scroll')

            yield Request(img_url, callback=self.get_img)

    def get_img(self, response):
        s = Selector(response)
        items = s.xpath('//div[@class="pic-box"]')
        for i in range(len(items)):
            ImgUrl = s.xpath('.//a/span/@data-img').extract()[i]
            comment = s.xpath('.//p[@class="comment"]/text()').extract()[i]
            file_name = str(comment) + '.gif'
            file_path = os.path.join(os.path.abspath('.'), 'imgs', file_name)
            request.urlretrieve(ImgUrl, file_path)
            print(ImgUrl, comment)
