import scrapy,os,random
from scrapy.selector import HtmlXPathSelector
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request
# from scrapy import log

opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
class PigSpider(scrapy.spiders.Spider):
    name = "pig"
    '''
    app name
    '''

    start_urls = [
        'http://www.mknight.cn',
    ]

    def parse(self,response):
        # print('response-url',response.url)
        hxs = HtmlXPathSelector(response)
        items = hxs.select('//section[@id="mainstay"]/div[@class="article well clearfix"]')
        # items = Selector(response=response).xpath('//div[@class="col-md-8 col-sm-7"]')
        # print(items)
        # print(len(items))
        for article in range(len(items)):
            title = hxs.select('//h1/a/text()').extract()[article]
            url = hxs.select('//h1/a/@href').extract()[article]
            # print(title,url)
            if title and url:

                try:
                    ab_src = 'http://www.mknight.cn' + url[0]
                    # print(url)
                    base_usr = 'http://www.mknight.cn'
                    html_url = base_usr + url
                    i = random.randrange(100)
                    s = 0
                    print(i)
                    while s < i:
                        opener.open(html_url)
                        s += 1
                        print(html_url)
                    # page = request.Request(html_url)
                    # print(page.headers)
                    # page.close()

                    # print(ab_src)
                    #page = request.urlopen(url[-4:-1])
                    #page.close()
                    # print(html)
                    """
                    file_name = url[-4:-1] + '.html'
                    file_path = os.path.join(os.path.abspath('.'), 'imgs', file_name)
                    print('new',file_name)
                    # request.urlretrieve(ab_src,file_path)
                    """
                except Exception as e:
                    print(e)

            for i in range(1,3):
                url = "http://www.mknight.cn/?page=" + str(i)
                # print(url)
                yield Request(url, callback=self.parse)

            '''
            # 获取所有的url，继续访问，并在其中寻找相同的url
            all_urls = hxs.select('//a/@href').extract()
            for url in all_urls:
                if url.startswith('?page='):
                    url = "http://39.106.51.169/" + url
                    yield Request(url=url, callback=self.parse)
            '''
