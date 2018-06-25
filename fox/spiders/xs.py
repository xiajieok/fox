import scrapy, os
from scrapy.selector import HtmlXPathSelector
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request


base_url = 'https://www.xiaoshuoli.com/i37935/'


class XSSpider(scrapy.spiders.Spider):
    name = "xs"
    start_urls = [
        'https://www.xiaoshuoli.com/i37935/',
    ]

    def parse(self, response):
        s = Selector(response)
        items = s.xpath('//body/div[@id="main"]/div[@class="box mt10"]/div[@class="book_list"]/dl/dd')
        # print('all',len(items),items)
        for li in range(len(items)):
            title = s.xpath('.//dd/a/text()').extract()[li]
            url = s.xpath('.//dd/a/@href').extract()[li]
            # print(title,url)
            url = base_url + url
            yield Request(url, callback=self.get_content)

    def get_content(self, response):
        s = Selector(response)
        title = s.xpath('//div[@class="h1title"]/h1/text()').extract()[0]
        content = s.xpath('//div[@id="htmlContent"]/text()').extract()
        msg = '###########################################################################'
        # print(type(content))
        # print(content)

        #
        print(title)
        file_name = title + '.txt'
        sss = '\n' + msg + '\n'
        f = open(file_name,'a+')
        f.write(sss)
        f.close()
        with open(file_name, 'ab+') as f:
            # title = msg + '\n' + title
            # print(type(title))
            f.write(title.encode('utf-8'))



        with open(file_name, 'ab+') as f:
            for i in content:
                # print(type(i))
                f.write(i.encode('utf-8'))


                # def get_img(self, response):
                #     s = Selector(response)
                #     items = s.xpath('//div[@class="pic-box"]')
                #     for i in range(len(items)):
                #         ImgUrl = s.xpath('.//a/span/@data-img').extract()[i]
                #         comment = s.xpath('.//p[@class="comment"]/text()').extract()[i]
                #         file_name = str(comment) + '.gif'
                #         file_path = os.path.join(os.path.abspath('.'), 'imgs', file_name)
                #         request.urlretrieve(ImgUrl, file_path)
                #         print(ImgUrl, comment)
