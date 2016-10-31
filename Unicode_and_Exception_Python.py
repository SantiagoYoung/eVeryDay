# -*- coding: utf-8 -*-
"""异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关----异常相关"""


#-- #捕获异常:
        try:
        except:                               # 捕获所有的异常 等同于except Exception:
        except name:                          # 捕获指定的异常
        except name, value:                   # 捕获指定的异常和额外的数据(实例)
        except (name1, name2):
        except (name1, name2), value:
        except name4 as X:
        else:                                 # 如果没有发生异常
        finally:                              # 总会执行的部分

        # 引发异常: raise子句(raise IndexError)
                raise <instance>                      # raise instance of a class, raise IndexError()
                raise <class>                         # make and raise instance of a class, raise IndexError
                raise                                 # reraise the most recent exception




# -- Python3.x中的异常链: raise exception from otherException
except Exception as X:
raise IndexError('Bad') from X

# -- assert子句: assert <test>, <data>
assert x < 0, 'x must be negative'






#-- with/as环境管理器:作为常见的try/finally用法模式的替代方案
    with expression [as variable], expression [as variable]:
    # 例子:
        with open('test.txt') as myfile:
            for line in myfile: print(line)
    # 等同于:
        myfile = open('test.txt')
        try:
            for line in myfile: print(line)
        finally:
            myfile.close()




            # -- 用户自定义异常: class Bad(Exception):.....
"""
Exception超类 / except基类即可捕获到其所有子类
Exception超类有默认的打印消息和状态 当然也可以定制打印显示:
"""


class MyBad(Exception):
    def __str__(self):
        return '定制的打印消息'


try:
    MyBad()
except MyBad as x:
    print(x)


# -- 用户定制异常数据
class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file


try:
    raise FormatError(42, 'test.py')
except FormatError as X:
    print('Error at ', X.file, X.line)


# 用户定制异常行为(方法):以记录日志为例
class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logger(self):
        open(self.logfile, 'a').write('Error at ', self.file, self.line)


try:
    raise FormatError(42, 'test.py')
except FormatError as X:
    X.logger()



#-- 异常层次
    BaseException
    +-- SystemExit
    +-- KeyboardInterrupt
    +-- GeneratorExit
    +-- Exception
        +-- StopIteration
        +-- ArithmeticError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        +-- LookupError
        +-- MemoryError
        +-- NameError
        +-- OSError
        +-- ReferenceError
        +-- RuntimeError
        +-- SyntaxError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        +-- Warning



"""Unicode和字节字符串---Unicode和字节字符串----Unicode和字节字符串----Unicode和字节字符串----Unicode和字节字符串----Unicode和字节字符串----Unicode和字节字符串"""


#-- Python的字符串类型
    """Python2.x"""
    # 1.str表示8位文本和二进制数据
    # 2.unicode表示宽字符Unicode文本
    """Python3.x"""
    # 1.str表示Unicode文本（8位或者更宽）
    # 2.bytes表示不可变的二进制数据
    # 3.bytearray是一种可变的bytes类型


#-- 字符编码方法
    """ASCII"""                   # 一个字节，只包含英文字符，0到127，共128个字符，利用函数可以进行字符和数字的相互转换
    ord('a')                      # 字符a的ASCII码为97，所以这里返回97
    chr(97)                       # 和上边的过程相反，返回字符'a'
    """Latin-1"""                 # 一个字节，包含特殊字符，0到255，共256个字符，相当于对ASCII码的扩展
    chr(196)                      # 返回一个特殊字符：Ä
    """Unicode"""                 # 宽字符，一个字符包含多个字节，一般用于亚洲的字符集，比如中文有好几万字
    """UTF-8"""                   # 可变字节数，小于128的字符表示为单个字节，128到0X7FF之间的代码转换为两个字节，0X7FF以上的代码转换为3或4个字节
    # 注意：可以看出来，ASCII码是Latin-1和UTF-8的一个子集
    # 注意：utf-8是unicode的一种实现方式，unicode、gbk、gb2312是编码字符集



#-- 查看Python中的字符串编码名称，查看系统的编码
    import encodings
    help(encoding)
    import sys
    sys.platform                  # 'win64'
    sys.getdefaultencoding()      # 'utf-8'
    sys.getdefaultencoding()      # 返回当前系统平台的编码类型
    sys.getsizeof(object)         # 返回object占有的bytes的大小


#-- 源文件字符集编码声明: 添加注释来指定想要的编码形式 从而改变默认值 注释必须出现在脚本的第一行或者第二行
    """说明：其实这里只会检查#和coding:utf-8，其余的字符都是为了美观加上的"""
    # _*_ coding: utf-8 _*_
    # coding = utf-8



#-- #编码: 字符串 --> 原始字节       #解码: 原始字节 --> 字符串


#-- Python3.x中的字符串应用
    s = '...'                     # 构建一个str对象，不可变对象
    b = b'...'                    # 构建一个bytes对象，不可变对象
    s[0], b[0]                    # 返回('.', 113)
    s[1:], b[1:]                  # 返回('..', b'..')
    B = B"""
        xxxx
        yyyy
        """
    # B = b'\nxxxx\nyyyy\n'
    # 编码，将str字符串转化为其raw bytes形式：
        str.encode(encoding = 'utf-8', errors = 'strict')
        bytes(str, encoding)




# 编码例子：
S = 'egg'
S.encode()  # b'egg'
bytes(S, encoding='ascii')  # b'egg'
# 解码，将raw bytes字符串转化为str形式：
bytes.decode(encoding='utf-8', errors='strict')
str(bytes_or_buffer[, encoding[, errors]])
# 解码例子：
B = b'spam'
B.decode()  # 'spam'
str(B)  # "b'spam'"，不带编码的str调用，结果为打印该bytes对象
str(B, encoding='ascii')  # 'spam'，带编码的str调用，结果为转化该bytes对象



#-- Python2.x的编码问题
    u = u'汉'
    print repr(u)                 # u'\xba\xba'
    s = u.encode('UTF-8')
    print repr(s)                 # '\xc2\xba\xc2\xba'
    u2 = s.decode('UTF-8')
    print repr(u2)                # u'\xba\xba'
    # 对unicode进行解码是错误的
    s2 = u.decode('UTF-8')        # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    # 同样，对str进行编码也是错误的
    u2 = s.encode('UTF-8')        # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 0: ordinal not in range(128)  # -- #文本文件: 根据Unicode编码来解释文件内容，要么是平台的默认编码，要么是指定的编码类型




# 二进制文件：表示字节值的整数的一个序列 open('bin.txt', 'rb')

# -- Unicode文件
s = 'A\xc4B\xe8C'  # s = 'A?BèC'  len(s) = 5
# 手动编码
l = s.encode('latin-1')  # l = b'A\xc4B\xe8C'  len(l) = 5
u = s.encode('utf-8')  # u = b'A\xc3\x84B\xc3\xa8C'  len(u) = 7
# 文件输出编码
open('latindata', 'w', encoding='latin-1').write(s)
l = open('latindata', 'rb').read()  # l = b'A\xc4B\xe8C'  len(l) = 5
open('uft8data', 'w', encoding='utf-8').write(s)
u = open('uft8data', 'rb').read()  # u = b'A\xc3\x84B\xc3\xa8C'  len(u) = 7
# 文件输入编码
s = open('latindata', 'r', encoding='latin-1').read()  # s = 'A?BèC'  len(s) = 5
s = open('latindata', 'rb').read().decode('latin-1')  # s = 'A?BèC'  len(s) = 5
s = open('utf8data', 'r', encoding='utf-8').read()  # s = 'A?BèC'  len(s) = 5
s = open('utf8data', 'rb').read().decode('utf-8')  # s = 'A?BèC'  len(s) = 5

"""其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他----其他"""


#-- Python实现任意深度的赋值 例如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'
    class MyDict(dict):
        def __setitem__(self, key, value):                 # 该函数不做任何改动 这里只是为了输出
            print('setitem:', key, value, self)
            super().__setitem__(key, value)
        def __getitem__(self, item):                       # 主要技巧在该函数
            print('getitem:', item, self)                  # 输出信息
            # 基本思路: a[1][2]赋值时 需要先取出a[1] 然后给a[1]的[2]赋值
            if item not in self:                           # 如果a[1]不存在 则需要新建一个dict 并使得a[1] = dict
                temp = MyDict()                            # 新建的dict: temp
                super().__setitem__(item, temp)            # 赋值a[1] = temp
                return temp                                # 返回temp 使得temp[2] = value有效
            return super().__getitem__(item)               # 如果a[1]存在 则直接返回a[1]
    # 例子:
        test = MyDict()
        test[0] = 'test'
        print(test[0])
        test[1][2] = 'test1'
        print(test[1][2])
        test[1][3] = 'test2'
        print(test[1][3])

#-- Python中的多维数组
    lists = [0] * 3                                        # 扩展list，结果为[0, 0, 0]
    lists = [[]] * 3                                       # 多维数组，结果为[[], [], []]，但有问题，往下看
    lists[0].append(3)                                     # 期望看到的结果[[3], [], []]，实际结果[[3], [3], [3]]，原因：list*n操作，是浅拷贝，如何避免？往下看
    lists = [[] for i in range(3)]                         # 多维数组，结果为[[], [], []]
    lists[0].append(3)                                     # 结果为[[3], [], []]
    lists[1].append(6)                                     # 结果为[[3], [6], []]
    lists[2].append(9)                                     # 结果为[[3], [6], [9]]
    lists = [[[] for j in range(4)] for i in range(3)]     # 3行4列，且每一个元素为[]







#-- 60个字符解决FizzBuzz:
    """写一个程序, 打印数字1到100, 3的倍数打印“Fizz”来替换这个数, 5的倍数打印“Buzz”, 既是3又是5的倍数的打印“FizzBuzz”"""
    for x in range(101):
        print("fizz"[x%3*4::]+"buzz"[x%5*4::] or x)        # 解释:最主要用到列表(字符串)的子表


































































































