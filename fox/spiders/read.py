import scrapy, os
from scrapy.selector import Selector
from scrapy.http import Request
from fox import items as ReadItem

import pdfkit

# pdf = os.path.join(os.path.abspath('.'), 'htmls')
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",  # 支持中文
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}
html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
        {content}
        </body>
        </html>
        """

base_url = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/'
all = os.path.join(os.path.abspath('.'), 'all.html')


class ReadSpider(scrapy.spiders.Spider):
    name = "read"
    start_urls = [
        'http://python3-cookbook.readthedocs.io/zh_CN/latest/',
    ]

    def parse(self, response):
        links = []
        s = Selector(response)
        items = s.xpath('//li[@class="toctree-l2"]/a')
        for i in range(len(items)):
            url = s.xpath('//li[@class="toctree-l2"]/a/@href').extract()[i]
            if 'c01' in url or 'c01' in url:
                c_url = base_url + url
                links.append(c_url)
            else:
                print('no', url)
        for link in links:
            print(link)
            yield Request(link, callback=self.get_content)


    def get_content(self, response):
        print('#########################获取HTML#########################')
        item = ReadItem.ReadItem()

        url = response.url
        print(response.url)
        # file_name = url.split('/')[5][1:] + url.split('/')[6][1:3] + '.html'
        # file_name = os.path.join(os.path.abspath('.'), 'htmls', file_name)
        # print(file_name)
        content = response.xpath('//div[@class="section"]').extract()[0]
        item['content'] = content
        item['url'] = response.url
        yield item




        # html = html_template.format(content=content)
        # with open(file_name, 'a+', encoding='utf-8') as f:
        #     f.write(html)
        # return self.save_pdf()


    # def save_pdf(self):
    #     print('#########################执行转化PDF文件#########################')
        # filedir = os.path.join(os.path.abspath('.'), 'htmls')
        # files = os.listdir(filedir)
        # desc_file = os.path.join(os.path.abspath('.'), 'all.html')
        # #
        # for i in files:
        #     # 遍历单个文件，读取行数
        #     print(i)
        #     cc = os.path.join(os.path.abspath('.'), 'htmls', i)
        #     f = open(cc, 'r', encoding='utf-8')
        #     file = f.read()
        #     with open(desc_file, 'a+', encoding='utf-8') as new:
        #         new.write(file)
        #     f.close()
        # options = {
        #     'page-size': 'Letter',
        #     'margin-top': '0.75in',
        #     'margin-right': '0.75in',
        #     'margin-bottom': '0.75in',
        #     'margin-left': '0.75in',
        #     'encoding': "UTF-8",
        #     'custom-header': [
        #         ('Accept-Encoding', 'gzip')
        #     ],
        #     'cookie': [
        #         ('cookie-name1', 'cookie-value1'),
        #         ('cookie-name2', 'cookie-value2'),
        #     ],
        #     'outline-depth': 10,
        # }
        #
        # pdf = pdfkit.from_file('all.html', 'out.pdf', options=options)
