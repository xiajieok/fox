import scrapy, os
from urllib import request
from scrapy.selector import Selector
from scrapy.http import Request
import urllib
import requests
import threading
import json

url = "http://www.mknight.cn"
file_path = os.path.join(os.path.abspath('.'), 'ip_pool.txt')
pool_file = os.path.join(os.path.abspath('.'), 'ip.json')
proxys = []

ip_list = []


class IPSpider(scrapy.spiders.Spider):
    global ip_list

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
        # 清空ip文件
        with open(pool_file, 'w') as f:
            f.truncate()
        # 多线程验证IP可用
        threads = []
        for i in proxys:
            thread = threading.Thread(target=self.check, args=(i,))
            threads.append(thread)
            thread.start()
        # 阻塞主进程，等待所有子线程结束
        for thread in threads:
            thread.join()
        tmp_dict = {}
        tmp_dict['server'] = ip_list
        with open(pool_file, 'w+') as f:
            json.dump(tmp_dict, f)

    def check(self, args):
        tmp = {}

        try:
            res = requests.get(url, proxies=args, timeout=1).headers
            ip = args['http']
            tmp['addr'] = ip
            ip_list.append(tmp)
        except Exception as e:
            pass
