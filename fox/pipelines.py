# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, re
from urllib import request
import pymysql


#
# class FoxPipeline(object):
#     def process_item(self, item, spider):
#         print('zhi xing  piplines')
#         ab_src = 'http://www.xiaohuar.com' + item['src']
#         file_name = item['name']
#         file_path = os.path.join(os.path.abspath('.'), 'imgs', file_name)
#         print(file_name)
#
#         request.urlretrieve(ab_src, file_path)
#         return item


class ZiruPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.40', user='ziru', passwd='ziru', db='ziru', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        query = self._conditional_insert(item)
        return item

    def _conditional_insert(self, item):
        uptown = item['site'].split()[0][3:].replace("]", "")
        part = item['site'][1:3]
        size = float(item["size"].replace('约', '').replace('㎡', ''))
        self.cur.execute(
                """insert into house (part,uptown,title,site,price,url,size,style,floor,share) values (%s,%s,%s ,%s, %s,%s,%s, %s, %s,%s)""",
                (part, uptown, item["title"], item["site"], item["price"], item["url"], size, item["style"],
                 item["floor"],
                 item["share"]))
        # self.cur.close()
        self.conn.commit()


class ReadPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.40', user='ziru', passwd='ziru', db='ziru', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        query = self._conditional_insert(item)
        return item

    def _conditional_insert(self, item):
        # 创建数据表SQL语句
        print('创建表')
        # sql = """CREATE TABLE readdoc (
        #  title  CHAR(64) NOT NULL,
        #  content  CHAR(0),
        #  url CHAR(64)
        #   )"""
        #
        # self.cur.execute(sql)
        # sql = """insert into readdoc (title,content,url) values(%s,%s,%s)""", (
        # item['title'], item['content'], item['lesson_url'])
        print('开始插入')
        print(type(item['title']),type(item['content']),type(item['lesson_url']))
        self.cur.execute("""insert into readdoc (title,content,url) values (%s,%s,%s)""",
                         (item['title'], item['content'], item['lesson_url']))
        print('完啦')

        self.conn.commit()
