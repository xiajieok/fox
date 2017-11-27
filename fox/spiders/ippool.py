import scrapy, os
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request
import urllib
import requests
import threading

url = "http://www.mknight.cn"
file_path = os.path.join(os.path.abspath('.'), 'ip_pool.txt')
pool_file = os.path.join(os.path.abspath('.'), 'ip.txt')
proxys = []


class IPSpider(scrapy.spiders.Spider):
    name = "ippool"
    start_urls = [
        'http://www.xicidaili.com/wt/',
    ]

    def parse(self, response):
        s = Selector(response)
        items = s.xpath('//table[@id="ip_list"]/tr')
        # print(items)
        for li in range(len(items) - 1):
            # print(li)
            ip = s.xpath('//table[@id="ip_list"]/tr/td[2]/text()').extract()[li]
            port = s.xpath('//table[@id="ip_list"]/tr/td[3]/text()').extract()[li]
            # print(ip)
            with open(file_path, 'a') as f:
                f.write("http://" + ip + ":" + port + "\n")
        for i in range(2, 100):
            url = "http://www.xicidaili.com/wt/" + str(i)
            # print(url)
            yield Request(url, callback=self.parse)
        # 多线程验证
        print('IP 获取完毕,开始验证')
        with open(file_path, 'r+') as f:
            for line in f.readlines():
                proxy_temp = {"http": line.strip('\n')}
                proxys.append(proxy_temp)
                # url = "http://ip.chinaz.com/getip.aspx"
        #清空ip文件
        with open(pool_file,'w') as f:
            f.truncate()
        #多线程验证IP可用
        threads = []
        for i in proxys:
            thread = threading.Thread(target=self.check, args=(i,))
            threads.append(thread)
            thread.start()
        # 阻塞主进程，等待所有子线程结束
        for thread in threads:
            thread.join()

    def check(self, args):

        try:
            res = requests.get(url, proxies=args, timeout=1).headers
            # print(args,'OK !!!')
            ip = args['http']
            proxy_support = urllib.request.ProxyHandler(args)
            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent','Mozilla/5.0')]
            html = opener.open(url,timeout= 1)
            with open(pool_file, 'a+') as f:
                f.write(ip + '\n')


        except Exception as e:
            pass
            # print(args,'NO')
            # print(e)
