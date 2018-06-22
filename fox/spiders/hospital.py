import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

base_url = 'http://yyk.99.com.cn/guangzhou/'


class HospitalSpider(scrapy.Spider):
    name = "hospital"
    allowed_domains = ["yyk.99.com.cn/"]
    start_urls = [
        "http://yyk.99.com.cn/guangzhou/",
    ]

    def parse(self, response):
        links = []
        s = Selector(response)
        items = s.xpath('//div[@class="tablist"]//ul/li/a')
        # 循环出所有医院URL
        for i in range(len(items)):
            url = s.xpath('//div[@class="tablist"]//ul/li/a/@href').extract()[i]
            # print(url)
            title = s.xpath('//div[@class="tablist"]//ul/li/a/@title').extract()[i]
            # print(title)
            yield Request(url, callback=self.get_msg)

    def get_msg(self, response):
        s = Selector(response)
        print(s)
        items = s.xpath('//div[@class="hpi_content clearbox"]/ul/li')
        for i in range(len(items)):
            msg = s.xpath('.//span//text()').extract()[i]
            print(msg)
