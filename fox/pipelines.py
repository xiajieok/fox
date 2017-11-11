# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
import pymysql
from twisted.enterprise import adbapi


class FoxPipeline(object):
    def process_item(self, item, spider):
        print('zhi xing  piplines')
        ab_src = 'http://www.xiaohuar.com' + item['src']
        file_name = item['name']
        file_path = os.path.join(os.path.abspath('.'), 'imgs', file_name)
        print(file_name)

        request.urlretrieve(ab_src, file_path)
        return item


class ZiruPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='XXXXXX', db='ziru', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        query = self._conditional_insert(item)
        return item

        # title= item['title']
        # site = item['site']
        # price = item['price']
        # url = item['src']
        # print(title,site,price)
        # pass

    def _conditional_insert(self, item):
        self.cur.execute(
            """insert into house (title,site,price,url,size,style,floor,share) values (%s, %s, %s,%s,%s, %s, %s,%s)""",
            (item["title"], item["site"], item["price"], item["url"], item["size"], item["style"], item["floor"],
             item["share"]))
        # self.cur.close()
        self.conn.commit()

# self.conn.close()
# log.msg("Item data in db: %s" % item, level=log.DEBUG
# class DBPipeline(object):
#
#     def __init__(self):
#         self.db_pool = adbapi.ConnectionPool('MySQLdb',
#                                              db='ziru',
#                                              user='root',
#                                              passwd='youxia',
#                                              cursorclass=pymysql.cursors.DictCursor,
#                                              use_unicode=True)
#
#     def process_item(self, item, spider):
#         query = self.db_pool.runInteraction(self._conditional_insert, item)
#         query.addErrback(self.handle_error)
#         return item
#
#     def _conditional_insert(self, tx, item):
#         tx.execute("select nid from company where company = %s", (item['company'][0],))
#         result = tx.fetchone()
#         if result:
#             pass
#         else:
#             phone_obj = phone_re.search(item['info'][0].strip())
#             phone = phone_obj.group() if phone_obj else ' '
#
#             mobile_obj = mobile_re.search(item['info'][1].strip())
#             mobile = mobile_obj.group() if mobile_obj else ' '
#
#             values = (
#                 item['company'][0],
#                 item['qq'][0],
#                 phone,
#                 mobile,
#                 item['info'][2].strip(),
#                 item['more'][0])
#             tx.execute("insert into company(company,qq,phone,mobile,address,more) values(%s,%s,%s,%s,%s,%s)", values)
