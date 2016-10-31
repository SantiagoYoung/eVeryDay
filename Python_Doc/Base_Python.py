# -*- coding: utf-8 -*-
obj = None
L = list
#寻求帮助：
    dir(obj) #简单的列出对象object所包含的方法名称，返回一个字符串列表
    help(obj.func) #查询obj.func的具体介绍和用法

#-- 测试类型的三种方法，推荐第三种
    if type(L) == type([]): print("L is list")
    if type(L) == list: print('L is list')
    if isinstance(L, list): print('L is list')

# -- python 数据类型： 哈希类型、不可哈希类型
    # -- 哈希类型，在原地不能改变的变量类型，不可变类型。
    # 可利用hash函数查看其hash值，也可以作为字典的key.
'''
        数字类型： int, float, decimal.Decimal, fractions.Fraction, complex
        字符串类型： str, bytes
        元组： tuple
        冻结集合： frozenset
        布尔类型： True, False
         None
'''
    # 不可hash类型： 原地可变类型： list, dic 和 set。
    # 它们不可以作为字典的key

# 数字常量
'''
    整数： 1234, -1234, 0, 999999999
    浮点数： 1.23, 1., 3.14e-10, 4E210, 4.0e+210
    八进制、十六进制、二进制数：0o177, 0x9ff, 0X9FF, 0b101010
    复数常量，也可以用complex（real, image)来创建 ： 3+4j
    将十进制数转化为十六进制、八进制、二进制表示的’字符串‘： hex(I), oct(I), bin(I)
    将字符串转化为整数，base为进制数：  int(string, base)
    # 2.x 中，有两种整数类型： 一般整数（32）和长整数(无穷精度）
    无穷大， 无穷小， 非数： float('inf'), float('-inf'), float('nan')
'''

# 数字的表达式操作符

    yield x     #生成器函数发送协议
    lambda args: expression   #匿名函数
    x if y else z   # 三元选择表达式
    x and y, x or y , not x   #逻辑 与， 或， 非
    x in y , x not in y       #成员对象测试
    x is y , x is not y       #对象实体测试
    x<y, x<=y, x>y, x==y, x!=y   #大小比较
    1 < a < 3                   #连续比较
    x|y , x&y, x^y             #位或， 位与， 位异或
    x<<y, x>>y                #位操作： x左移，右移y位
    +,-,*,/, //, %, **        #真除法，floor除法：返回不大于真除法结果的整数值，取余，幂运算
    -x, +x, ~x                #已元减法、识别、取反
    x[i], x[i:j:k]            #索引、分片、调用
    int(3.14), float(3)       #强制类型转换

# ---- 整数可以利用bit_length函数测试所占的位数
a = 1; a.bit_length()  1
a = 1024 a.bit_length() 11


#-- repr 和 str 显示格式的区别
'''
repr格式： 默认的交互模式回显，产生的结果看起来它们就像是代码
str格式：  打印语句，转化成一种对用户更加友好的格式
'''



# -- 数字相关的模块
    # math模块
    #Decimal 模块； 小数模块
    import decimal
    from decimal import Decimal
    Decimal('0.01') + Decimal('0.02')
    decimal.getcontext().prec = 4
    # Fraction模块： 分数模块
    from fractions import Fraction
    x = Fraction(4, 6)
    x = Fraction('0.25')


# --  集合set
'''
   set 是一个无序不重复元素集，基本功能包括关系测试和消除重复元素。
   set 支持union（联合），intersection（交）, difference(差）和systemmetric difference(对称差集）等数学运算
   set 支持 x in set, len(set), for x in set
   set 不记录元素位置或者插入点，因此不支持indexing, slicing，或者其他序列操作
'''
s = set([2, 3, 4])              # 创建一个数值集合，返回{3, 5, 9, 10}
t = set('Hello')                # 创建一个唯一字符的集合返回{}
a = t | s  ;  t.union(s)          # t 和 s的并集
b = t & s  ;  t.intersection(s)   # t 和 s的交集
c = t - s;    t.difference(s)     # 求差集（项在t中, 但不在s中）
d = t ^ s;    t.symmetric_difference(s)      # 对称差集（项在t或s中, 但不会同时出现在二者中）
t.add('x'); t.remove('g')         # 增加/删除一个item
t.update([10, 24, 23])           # 利用[......]更新s集合
x in s, x not in s  # 集合中是否存在某个值
s.issubset(t); s.issuperset(t); s.copy(); s.discard(x); s.clear()
    {x**2 for x in [1, 2, 3, 4]}                 # 集合解析，结果：{16, 1, 4, 9}
    {x for x in 'spam'}                          # 集合解析，结果：{'a', 'p', 's', 'm'}



# ---  集合frozenset， 不可变对象
"""
set是可变对象，即不存在hash值，不能作为字典的键。同样的还有list、tuple等
frozenset是不可变对象，即存在hash值，可以作为字典的键值
frozenset对象没有add、remove等方法，但有union/intersection/difference等方法
"""
a = set([1, 2, 3])
b = set()
b.add(a)  # error: set是不可哈希类型
b.add(frozenset(a))  # ok，将set变为frozenset，可哈希



#---- 布尔类型 bool
type(True)                   # 返回<class 'bool'>
isinstance(False, int)       # bool类型属于整形，所以返回True
True == 1; True is 1         # 输出(True, False)


# -- 动态类型简介
"""
变量名通过引用，指向对象。
Python中的‘类型’属于对象，而不是变量，每个对象都包含有头部信息，
比如”类型提示符“ ， ”引用计数器“ 等
"""

# 共享引用以及在原处修改： 对于可变对象，要注意尽量不要共享引用！
#共享引用和相等测试：


L = [1], M = [1], L is M            # 返回False
L = M = [1, 2, 3], L is M           # 返回True，共享引用
#增强赋值和共享引用：普通+号会生成新的对象，而增强赋值+=会在原处修改
L = M = [1, 2]
L = L + [3, 4]                      # L = [1, 2, 3, 4], M = [1, 2]
L += [3, 4]                         # L = [1, 2, 3, 4], M = [1, 2, 3, 4]




# -- 常见字符串常量和表达式
S = ''                                  # 空字符串
S = "spam’s"                            # 双引号和单引号相同
S = "s\np\ta\x00m"                      # 转义字符
S = """spam"""                          # 三重引号字符串，一般用于函数说明
S = r'\temp'                            # Raw字符串，不会进行转义，抑制转义
S = b'Spam'                             # Python3中的字节字符串
S = u'spam'                             # Python2.6中的Unicode字符串
s1+s2, s1*3, s[i], s[i:j], len(s)       # 字符串操作
'a %s parrot' % 'kind'                  # 字符串格式化表达式
'a {0} parrot'.format('kind')           # 字符串格式化方法
for x in s: print(x)                    # 字符串迭代，成员关系
[x*2 for x in s]                        # 字符串列表解析
','.join(['a', 'b', 'c'])               # 字符串输出，结果：a,b,c


#-- 内置str处理函数：
str1 = "stringobject"
str1.upper(); str1.lower(); str1.swapcase(); str1.capitalize(); str1.title()        # 全部大写，全部小写、大小写转换，首字母大写，每个单词的首字母都大写
str1.ljust(width)                       # 获取固定长度，左对齐，右边不够用空格补齐
str1.rjust(width)                       # 获取固定长度，右对齐，左边不够用空格补齐
str1.center(width)                      # 获取固定长度，中间对齐，两边不够用空格补齐
str1.zfill(width)                       # 获取固定长度，右对齐，左边不足用0补齐
str1.find('t',start,end)                # 查找字符串，可以指定起始及结束位置搜索
str1.rfind('t')                         # 从右边开始查找字符串
str1.count('t')                         # 查找字符串出现的次数
#上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
str1.replace('old','new')               # 替换函数，替换old为new，参数中可以指定maxReplaceTimes，即替换指定次数的old为new
str1.strip(); str1.lstrip(); str1.rstrip(); str1.strip('d'); str1.lstrip('d'); str1.rstrip('d')
str1.startswith('start')                # 是否以start开头
str1.endswith('end')                    # 是否以end结尾
str1.isalnum(); str1.isalpha(); str1.isdigit(); str1.islower(); str1.isupper()      # 判断字符串是否全为字符、数字、大写、小写



#-- 三重引号编写多行字符串块，并且在代码折行处嵌入换行字符\n
mantra = """hello world
        hello python
        hello my friend"""
# mantra为"""hello world \n hello python \n hello my friend"""


''''''''''''''''''''
# -- 索引和分片：
S[0], S[len(S)–1], S[-1]  # 索引
S[1:3], S[1:], S[:-1], S[1:10:2]  # 分片，第三个参数指定步长

# -- 字符串转换工具：
int('42'), str(42)  # 返回(42, '42')
float('4.13'), str(4.13)  # 返回(4.13, '4.13')
ord('s'), chr(115)  # 返回(115, 's')
int('1001', 2)  # 将字符串作为二进制数字，转化为数字，返回13
bin(13), oct(13), hex(13)  # 将整数转化为二进制/八进制/十六进制字符串，返回('1001', '0o15', '0xd')

# -- 另类字符串连接
name = "wang" "hong"  # 单行，name = "wanghong"
name = "wang" \
       "hong"  # 多行，name = "wanghong"





#-- Python中的字符串格式化实现1--字符串格式化表达式
"""
基于C语言的'print'模型，并且在大多数的现有的语言中使用。
通用结构：%[(name)][flag][width].[precision]typecode
"""
"this is %d %s bird" % (1, 'dead')                          # 一般的格式化表达式
"%s---%s---%s" % (42, 3.14, [1, 2, 3])                      # 字符串输出：'42---3.14---[1, 2, 3]'
"%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)         # 对齐方式及填充："1234...  1234...1234  ...001234"
x = 1.23456789
"%e | %f | %g" % (x, x, x)                                  # 对齐方式："1.234568e+00 | 1.234568 | 1.23457"
"%6.2f*%-6.2f*%06.2f*%+6.2f" % (x, x, x, x)                 # 对齐方式：'  1.23*1.23  *001.23* +1.23'
"%(name1)d---%(name2)s" % {"name1":23, "name2":"value2"}    # 基于字典的格式化表达式
"%(name)s is %(age)d" % vars()                              # vars()函数调用返回一个字典，包含了所有本函数调用时存在的变量


#-- Python中的字符串格式化实现2--字符串格式化调用方法
    # 普通调用
    "{0}, {1} and {2}".format('spam', 'ham', 'eggs')            # 基于位置的调用
    "{motto} and {pork}".format(motto = 'spam', pork = 'ham')   # 基于Key的调用
    "{motto} and {0}".format('ham', motto = 'spam')               # 混合调用
    # 添加键 属性 偏移量 (import sys)
    "my {1[spam]} runs {0.platform}".format(sys, {'spam':'laptop'})                 # 基于位置的键和属性
    "{config[spam]} {sys.platform}".format(sys = sys, config = {'spam':'laptop'})   # 基于Key的键和属性
    "first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C'])                       # 基于位置的偏移量
    # 具体格式化
    "{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)   # 输出'3.141590e+00, 3.142e+00, 3.14159'
    "{fieldname:format_spec}".format(......)
    # 说明:
    """
        fieldname是指定参数的一个数字或关键字, 后边可跟可选的".name"或"[index]"成分引用
        format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
        fill        ::=  <any character>              #填充字符
        align       ::=  "<" | ">" | "=" | "^"        #对齐方式
        sign        ::=  "+" | "-" | " "              #符号说明
        width       ::=  integer                      #字符串宽度
        precision   ::=  integer                      #浮点数精度
        type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    """
    # 例子:
        '={0:10} = {1:10}'.format('spam', 123.456)    # 输出'=spam       =    123.456'
        '={0:>10}='.format('test')                    # 输出'=      test='
        '={0:<10}='.format('test')                    # 输出'=test      ='
        '={0:^10}='.format('test')                    # 输出'=   test   ='
        '{0:X}, {1:o}, {2:b}'.format(255, 255, 255)   # 输出'FF, 377, 11111111'
        'My name is {0:{1}}.'.format('Fred', 8)       # 输出'My name is Fred    .'  动态指定参数



#-- 常用列表常量和操作
#-- 常用列表常量和操作

L = [[1,2], 'string', {}]  #嵌套列表
L = list()                  #列表初始化
L = list(range(1,4))       #列表初始化
list(map(ord, 'spam'))     #列表解析
len(L)                     #列表长度
L.count(value)  # 求列表中某个值的个数
L.append(obj)  # 向列表的尾部添加数据，比如append(2)，添加元素2
L.insert(index, obj)  # 向列表的指定index位置添加数据，index及其之后的数据后移
L.extend(interable)  # 通过添加iterable中的元素来扩展列表，比如extend([2])，添加元素2，注意和append的区别
L.index(value, [start, [stop]])  # 返回列表中值value的第一个索引
L.pop([index])  # 删除并返回index处的元素，默认为删除并返回最后一个元素
L.remove(value)  # 删除列表中的value值，只删除第一次出现的value的值
L.reverse()  # 反转列表
L.sort(cmp=None, key=None, reverse=False)  # 排序列表
a = [1, 2, 3], b = a[10:]  # 注意，这里不会引发IndexError异常，只会返回一个空的列表[]
a = [], a += [1]  # 这里实在原有列表的基础上进行操作，即列表的id没有改变
a = [], a = a + [1]  # 这里最后的a要构建一个新的列表，即a的id发生了变化


#-- 用切片来删除序列的某一段
    a = [1, 2, 3, 4, 5, 6, 7]
    a[1:4] = []                                       # a = [1, 5, 6, 7]
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    del a[::2]                                        # 去除偶数项(偶数索引的)，a = [1, 3, 5, 7]


#-- 用切片来删除序列的某一段
    a = [1, 2, 3, 4, 5, 6, 7]
    a[1:4] = []                                       # a = [1, 5, 6, 7]
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    del a[::2]                                        # 去除偶数项(偶数索引的)，a = [1, 3, 5, 7]



#-- 常用字典常量和操作 #-- 常用字典常量和操作 #-- 常用字典常量和操作

D = {}
D = {'spam':2, 'tol':{'ham':1}}                   # 嵌套字典
D = dict.fromkeys(['s', 'd'], 8)                  # {'d': 8, 's': 8}
D = dict(name = 'tom', age = 12)                  # {'age': 12, 'name': 'tom'}
D = dict([('name', 'tom'), ('age', 12)])          # {'age': 12, 'name': 'tom'}
D = dict(zip(['name', 'age'], ['tom', 12]))       # {'age': 12, 'name': 'tom'}
D.keys(); D.values(); D.items()                   # 字典键、值以及键值对
D.get(key, default)                               # get函数
D.update(D_other)                                 # 合并字典，如果存在相同的键值，D_other的数据会覆盖掉D的数据
D.pop(key, [D])                                   # 删除字典中键值为key的项，返回键值为key的值，如果不存在，返回默认值D，否则异常
D.popitem()                                       # pop字典中的一项（一个键值对）
D.setdefault(k[, d])                              # 设置D中某一项的默认值。如果k存在，则返回D[k]，否则设置D[k]=d，同时返回D[k]。
del D                                             # 删除字典
del D['key']                                      # 删除字典的某一项
if key in D:   if key not in D:                   # 测试字典键是否存在
# 字典注意事项：（1）对新索引赋值会添加一项（2）字典键不一定非得是字符串，也可以为任何的不可变对象



#-- 字典解析
    D = {k:8 for k in ['s', 'd']}                     # {'d': 8, 's': 8}
    D = {k:v for (k, v) in zip(['name', 'age'], ['tom', 12])}


#-- 字典的特殊方法__missing__：当查找找不到key时，会执行该方法
    class Dict(dict):
        def __missing__(self, key):
            self[key] = []
            return self[key]
    dct = Dict()
    dct["foo"].append(1)    # 这有点类似于collections.defalutdict
    dct["foo"]              # [1]




#  -- 文件基本操作
output = open(r'C:\spam', 'w')  # 打开输出文件，用于写
input = open('data', 'r')  # 打开输入文件，用于读。打开的方式可以为'w', 'r', 'a', 'wb', 'rb', 'ab'等
fp.read([size])  # size为读取的长度，以byte为单位
fp.readline([size])  # 读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])  # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长。
fp.readable()  # 是否可读
fp.write(str)  # 把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)  # 把seq的内容全部写到文件中(多行一次性写入)
fp.writeable()  # 是否可写
fp.close()  # 关闭文件。
fp.flush()  # 把缓冲区的内容写入硬盘
fp.fileno()  # 返回一个长整型的”文件标签“
fp.isatty()  # 文件是否是一个终端设备文件（unix系统中的）
fp.tell()  # 返回文件操作标记的当前位置，以文件的开头为原点
fp.next()  # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[, whence])  # 将文件打操作标记移到offset的位置。whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。
fp.seekable()  # 是否可以seek
fp.truncate([size])  # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
for line in open('data'):
    print(line)  # 使用for语句，比较适用于打开比较大的文件
open('f.txt', encoding='latin-1')  # Python3.x Unicode文本文件
open('f.bin', 'rb')  # Python3.x 二进制bytes文件
# 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等

# -- 其他
# Python中的真假值含义：1. 数字如果非零，则为真，0为假。 2. 其他对象如果非空，则为真
# 通常意义下的类型分类：1. 数字、序列、映射。 2. 可变类型和不可变类型



