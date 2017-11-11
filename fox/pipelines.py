# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

class FoxPipeline(object):
    def process_item(self, item, spider):
        print('zhi xing  piplines')
        ab_src = 'http://www.xiaohuar.com' + item['src']
        file_name = item['name']
        file_path = os.path.join(os.path.abspath('.'),'imgs', file_name)
        print(file_name)

        request.urlretrieve(ab_src, file_path)
        return item
