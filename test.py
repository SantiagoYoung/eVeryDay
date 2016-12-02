# -*- coding: utf-8 -*-
'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。

1. 列出所有文件，并且排除不是.py的文件
2. 遍历py文件
3. 匹配 空白行， 注释行
4. 注释行包括 以 # 开头 和 '' 开头和结尾的

               怎么匹配 三个字符串开头的注释？
'''
# re.match(r"^'''.*'''$", line, re.DOTALL):
import os
import re

doc_list = os.listdir('/home/neon/eVeryDay')
py_doc =[]
for doc in doc_list:
    m = re.match('.*\.py$', doc)
    if m:
        py_doc.append(m.group())




with open('/home/neon/eVeryDay/Caculate.py', 'r') as f:
    total = 1
    comment = 0
    blank = 1
    code = 0
    # from copy import deepcopy
    #
    # f2 = deepcopy(f)






    # print re.match(r"^'''.*'''$", f2.read(), re.DOTALL)

    for line in f.readlines():
        total += 1
        if re.match('^#.*', line):
            comment += 1
        if re.match(r"^$", line):
            blank += 1
        if re.match(r'^.*',line):
            code += 1


    # if re.match('^#.*', f):
    #     comment += 1
    # if re.match(r'^$', f):
    #     blank += 1
    # if re.match(r"^'''.*'''", f, re.DOTALL):
    #     comment += 1

print 'total',total
print 'comment',comment
print 'blank',blank
print 'code', code






with open('test.html','r') as f:

    print re.findall(r'<p>.*?</p>', f.read(), re.DOTALL)

    print re.findall(r'<a>.*?</a>', f.read(), re.DOTALL)


with open('/home/neon/eVeryDay/Caculate.py', 'r') as F:


    print 'hello',(re.findall(r"'''.*?'''", F.read(), re.DOTALL))



