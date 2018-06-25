# coding=utf-8
import os

f = open('../result.txt', 'wb')
filenames = os.listdir()
for filename in filenames:
    # filepath = filedir+'/'+filename
    # 遍历单个文件，读取行数
    for line in open(filename,'rb'):
        f.write(line)
# 关闭文件
f.close()
