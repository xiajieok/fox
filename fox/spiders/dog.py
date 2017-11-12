import scrapy,re
from scrapy.selector import Selector
from scrapy.http import Request
from fox import items as fox_items


class PigSpider(scrapy.spiders.Spider):
    name = "dog"
    '''
    app name
    '''

    start_urls = [
        'http://www.ziroom.com/z/nl/z3.html',
    ]

    def parse(self, response):
        s = Selector(response)
        items = s.xpath('//ul[@id="houseList"]/li[@class="clearfix"]')
        for house in range(len(items)):
            title = s.xpath('.//div[@class="txt"]/h3/a/text()').extract()[house]
            url = s.xpath('.//div[@class="txt"]/h3/a/@href').extract()[house][2:]
            site = s.xpath('.//div[@class="txt"]/h4/a/text()').extract()[house]
            size = s.xpath('.//div[@class="txt"]/div[@class="detail"]/p[1]/span[1]/text()').extract()[house]
            floor = s.xpath('.//div[@class="txt"]/div[@class="detail"]/p[1]/span[2]/text()').extract()[house]
            style = s.xpath('.//div[@class="txt"]/div[@class="detail"]/p[1]/span[3]/text()').extract()[house]
            share = s.xpath('.//div[@class="txt"]/div[@class="detail"]/p[1]/span[4]/text()').extract()[house]
            price_list = s.xpath('.//div[@class="priceDetail"]/p[@class="price"]/text()').extract()

            for i in price_list:
                if "\n                        " in price_list:
                    price_list.remove("\n                        ")
            price = price_list[house]
            try:

                item = fox_items.FoxItem()
                item['title'] = title
                item['site'] = site
                item['price'] = price.split()[1]
                item['url'] = url
                item['size'] = size
                item['floor'] = floor
                item['style'] = style
                item['share'] = share
                # print(item)
                print('******************', title)
                yield item
            except Exception as e:
                print(e)
        # 获取所有的url，继续访问，并在其中寻找相同的url
        all_urls = s.select('//a/@href').extract()
        # print(all_urls)
        for i in range(2, 51):
            url = 'http://www.ziroom.com/z/nl/z3.html?p=' + str(i)
            yield Request(url, callback=self.parse)
