import os
import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'outline-depth': 10,
}

filedir = os.path.join(os.path.abspath('.'), 'htmls')
files = os.listdir(filedir)
desc_file = os.path.join(os.path.abspath('.'), 'all.html')
#
for i in files:
    # 遍历单个文件，读取行数
    print(i)
    cc = os.path.join(os.path.abspath('.'), 'htmls', i)
    with open(cc, 'r', encoding='utf-8') as f:
        with open(desc_file, 'a+', encoding='utf-8') as new:
            new.write(f.read())

pdf = pdfkit.from_file('all.html', 'out.pdf', options=options)
