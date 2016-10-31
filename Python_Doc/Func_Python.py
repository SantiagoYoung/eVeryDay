# -*- coding: utf-8 -*-


"""函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则----函数语法规则"""

#-- 函数相关的语句和表达式
    myfunc('spam')                     # 函数调用
    def myfunc():                      # 函数定义
    return None                        # 函数返回值
    global a                           # 全局变量
    nonlocal x                         # 在函数或其他作用域中使用外层（非全局）变量
    yield x                            # 生成器函数返回
    lambda                             # 匿名函数


#-- Python函数变量名解析:LEGB原则，即:
    """
    local(functin) --> encloseing function locals --> global(module) --> build-in(python)
    说明:以下边的函数maker为例 则相对于action而言 X为Local N为Encloseing
    """


#-- 嵌套函数举例:工厂函数
    def maker(N):
        def action(X):
            return X ** N
        return action
    f = maker(2)                       # pass 2 to N
    f(3)                               # 9, pass 3 to X

#-- 嵌套函数举例:lambda实例
    def maker(N):
        action = (lambda X: X**N)
        return action
    f = maker(2)                       # pass 2 to N
    f(3)                               # 9, pass 3 to X



#-- nonlocal和global语句的区别
    # nonlocal应用于一个嵌套的函数的作用域中的一个名称 例如:
    start = 100
    def tester(start):
        def nested(label):
            nonlocal start             # 指定start为tester函数内的local变量 而不是global变量start
            print(label, start)
            start += 3
        return nested
    # global为全局的变量 即def之外的变量
    def tester(start):
        def nested(label):
            global start               # 指定start为global变量start
            print(label, start)
            start += 3
        return nested

# Keyword-Only参数:出现在*args之后 必须用关键字进行匹配
    def keyOnly(a, *b, c): print('')   # c就为keyword-only匹配 必须使用关键字c = value匹配
    def keyOnly(a, *, b, c): ......    # b c为keyword-only匹配 必须使用关键字匹配
    def keyOnly(a, *, b = 1): ......   # b有默认值 或者省略 或者使用关键字参数b = value  # -- 可变参数匹配: * 和 **
def f(*args): print(args)  # 在元组中收集不匹配的位置参数


f(1, 2, 3)  # 输出(1, 2, 3)


def f(**args): print(args)  # 在字典中收集不匹配的关键字参数


f(a=1, b=2)  # 输出{'a':1, 'b':2}


def f(a, *b, **c): print(a, b, c)  # 两者混合使用


f(1, 2, 3, x=4, y=5)  # 输出1, (2, 3), {'x':4, 'y':5}

# -- 函数调用时的参数解包: * 和 ** 分别解包元组和字典
func(1, *(2, 3)) <= = > func(1, 2, 3)
func(1, **{'c': 3, 'b': 2}) <= = > func(1, b=2, c=3)
func(1, *(2, 3), **{'c': 3, 'b': 2}) <= = > func(1, 2, 3, b=2, c=3)



#-- 函数注解: 编写在def头部行 主要用于说明参数范围、参数类型、返回值类型等
    def func(a:'spam', b:(1, 10), c:float) -> int :
        print(a, b, c)
    func.__annotations__               # {'c':<class 'float'>, 'b':(1, 10), 'a':'spam', 'return':<class 'int'>}
    # 编写注解的同时 还是可以使用函数默认值 并且注解的位置位于=号的前边
    def func(a:'spam'='a', b:(1, 10)=2, c:float=3) -> int :
        print(a, b, c)

#-- 匿名函数:lambda
    f = lambda x, y, z : x + y + z     # 普通匿名函数，使用方法f(1, 2, 3)
    f = lambda x = 1, y = 1: x + y     # 带默认参数的lambda函数
    def action(x):                     # 嵌套lambda函数
        return (lambda y : x + y)
    f = lambda: a if xxx() else b      # 无参数的lambda函数，使用方法f()


# -- lambda函数与map filter reduce函数的结合
list(map((lambda x: x + 1), [1, 2, 3]))  # [2, 3, 4]
list(filter((lambda x: x > 0), range(-4, 5)))  # [1, 2, 3, 4]
functools.reduce((lambda x, y: x + y), [1, 2, 3])  # 6
functools.reduce((lambda x, y: x * y), [2, 3, 4])  # 24




#-- 生成器函数:yield VS return
    def gensquare(N):
        for i in range(N):
            yield i** 2                # 状态挂起 可以恢复到此时的状态
    for i in gensquare(5):             # 使用方法
        print(i, end = ' ')            # [0, 1, 4, 9, 16]
    x = gensquare(2)                   # x是一个生成对象
    next(x)                            # 等同于x.__next__() 返回0
    next(x)                            # 等同于x.__next__() 返回1
    next(x)                            # 等同于x.__next__() 抛出异常StopIteration



#-- 生成器表达式:小括号进行列表解析
    G = (x ** 2 for x in range(3))     # 使用小括号可以创建所需结果的生成器generator object
    next(G), next(G), next(G)          # 和上述中的生成器函数的返回值一致
    #（1）生成器(生成器函数/生成器表达式)是单个迭代对象
    G = (x ** 2 for x in range(4))
    I1 = iter(G)                       # 这里实际上iter(G) = G
    next(I1)                           # 输出0
    next(G)                            # 输出1
    next(I1)                           # 输出4
    #（2）生成器不保留迭代后的结果
    gen = (i for i in range(4))
    2 in gen                           # 返回True
    3 in gen                           # 返回True
    1 in gen                           # 返回False，其实检测2的时候，1已经就不在生成器中了，即1已经被迭代过了，同理2、3也不在了



#-- 本地变量是静态检测的
    X = 22                             # 全局变量X的声明和定义
    def test():
        print(X)                       # 如果没有下一语句 则该句合法 打印全局变量X
        X = 88                         # 这一语句使得上一语句非法 因为它使得X变成了本地变量 上一句变成了打印一个未定义的本地变量(局部变量)
        if False:                      # 即使这样的语句 也会把print语句视为非法语句 因为:
            X = 88                     # Python会无视if语句而仍然声明了局部变量X
    def test():                        # 改进
        global X                       # 声明变量X为全局变量
        print(X)                       # 打印全局变量X
        X = 88                         # 改变全局变量X



#-- 函数的默认值是在函数定义的时候实例化的 而不是在调用的时候 例子:
    def foo(numbers=[]):               # 这里的[]是可变的
        numbers.append(9)
        print(numbers)
    foo()                              # first time, like before, [9]
    foo()                              # second time, not like before, [9, 9]
    foo()                              # third time, not like before too, [9, 9, 9]
    # 改进:
    def foo(numbers=None):
        if numbers is None: numbers = []
        numbers.append(9)
        print(numbers)
    # 另外一个例子 参数的默认值为不可变的:
    def foo(count=0):                  # 这里的0是数字, 是不可变的
        count += 1
        print(count)
    foo()                              # 输出1
    foo()                              # 还是输出1
    foo(3)                             # 输出4
    foo()                              # 还是输出1



"""函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子----函数例子"""

"""数学运算类"""
abs(x)  # 求绝对值，参数可以是整型，也可以是复数，若参数是复数，则返回复数的模
complex([real[, imag]])  # 创建一个复数
divmod(a, b)  # 分别取商和余数，注意：整型、浮点型都可以
float([x])  # 将一个字符串或数转换为浮点数。如果无参数将返回0.0
int([x[, base]])  # 将一个字符串或浮点数转换为int类型，base表示进制
long([x[, base]])  # 将一个字符串或浮点数转换为long类型
pow(x, y)  # 返回x的y次幂
range([start], stop[, step])  # 产生一个序列，默认从0开始
round(x[, n])  # 四舍五入
sum(iterable[, start])  # 对集合求和
oct(x)  # 将一个数字转化为8进制字符串
hex(x)  # 将一个数字转换为16进制字符串
chr(i)  # 返回给定int类型对应的ASCII字符
unichr(i)  # 返回给定int类型的unicode
ord(c)  # 返回ASCII字符对应的整数
bin(x)  # 将整数x转换为二进制字符串
bool([x])  # 将x转换为Boolean类型



"""集合类操作"""
    basestring()                        # str和unicode的超类，不能直接调用，可以用作isinstance判断
    format(value [, format_spec])       # 格式化输出字符串，格式化的参数顺序从0开始，如“I am {0},I like {1}”
    enumerate(sequence[, start=0])      # 返回一个可枚举的对象，注意它有第二个参数
    iter(obj[, sentinel])               # 生成一个对象的迭代器，第二个参数表示分隔符
    max(iterable[, args...][key])       # 返回集合中的最大值
    min(iterable[, args...][key])       # 返回集合中的最小值
    dict([arg])                         # 创建数据字典
    list([iterable])                    # 将一个集合类转换为另外一个集合类
    set()                               # set对象实例化
    frozenset([iterable])               # 产生一个不可变的set
    tuple([iterable])                   # 生成一个tuple类型
    str([object])                       # 转换为string类型
    sorted(iterable[, cmp[, key[, reverse]]])             # 集合排序
        L = [('b',2),('a',1),('c',3),('d',4)]
        sorted(L, key=lambda x: x[1]), reverse=True)      # 使用Key参数和reverse参数
        sorted(L, key=lambda x: (x[0], x[1]))             # 使用key参数进行多条件排序，即如果x[0]相同，则比较x[1]


"""逻辑判断"""
all(iterable)  # 集合中的元素都为真的时候为真，特别的，若为空串返回为True
any(iterable)  # 集合中的元素有一个为真的时候为真，特别的，若为空串返回为False
cmp(x, y)  # 如果x < y ,返回负数；x == y, 返回0；x > y,返回正数

"""IO操作"""
file(filename[, mode[, bufsize]])  # file类型的构造函数。
input([prompt])  # 获取用户输入，推荐使用raw_input，因为该函数将不会捕获用户的错误输入
raw_input([prompt])  # 设置输入，输入都是作为字符串处理
open(name[, mode[, buffering]])  # 打开文件，与file有什么不同？推荐使用open









"""其他"""
    callable(object)                    # 检查对象object是否可调用
    classmethod(func)                   # 用来说明这个func是个类方法
    staticmethod(func)                  # 用来说明这个func为静态方法
    dir([object])                       # 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
    help(obj)                           # 返回obj的帮助信息
    eval(expression)                    # 计算表达式expression的值，并返回
    exec(str)                           # 将str作为Python语句执行
    execfile(filename)                  # 用法类似exec()，不同的是execfile的参数filename为文件名，而exec的参数为字符串。
    filter(function, iterable)          # 构造一个序列，等价于[item for item in iterable if function(item)]，function返回值为True或False的函数
        list(filter(bool, range(-3, 4)))# 返回[-3, -2, -1, 1, 2, 3], 没有0
    hasattr(object, name)               # 判断对象object是否包含名为name的特性
    getattr(object, name [, defalut])   # 获取一个类的属性
    setattr(object, name, value)        # 设置属性值
    delattr(object, name)               # 删除object对象名为name的属性
    globals()                           # 返回一个描述当前全局符号表的字典
    hash(object)                        # 如果对象object为哈希表类型，返回对象object的哈希值
    id(object)                          # 返回对象的唯一标识，一串数字
    isinstance(object, classinfo)       # 判断object是否是class的实例
        isinstance(1, int)              # 判断是不是int类型
        isinstance(1, (int, float))     # isinstance的第二个参数接受一个元组类型
    issubclass(class, classinfo)        # 判断class是否为classinfo的子类
    locals()                            # 返回当前的变量列表
    map(function, iterable, ...)        # 遍历每个元素，执行function操作
        list(map(abs, range(-3, 4)))    # 返回[3, 2, 1, 0, 1, 2, 3]
    next(iterator[, default])           # 类似于iterator.next()
    property([fget[, fset[, fdel[, doc]]]])           # 属性访问的包装类，设置后可以通过c.x=value等来访问setter和getter
    reduce(function, iterable[, initializer])         # 合并操作，从第一个开始是前两个参数，然后是前两个的结果与第三个合并进行处理，以此类推
        def add(x,y):return x + y
        reduce(add, range(1, 11))                     # 返回55 (注:1+2+3+4+5+6+7+8+9+10 = 55)
        reduce(add, range(1, 11), 20)                 # 返回75
    reload(module)                      # 重新加载模块
    repr(object)                        # 将一个对象变幻为可打印的格式
    slice(start, stop[, step])          # 产生分片对象
    type(object)                        # 返回该object的类型
    vars([object])                      # 返回对象的变量名、变量值得字典
        a = Class();                    # Class为一个空类
        a.name = 'qi', a.age = 9
        vars(a)                         # {'name':'qi', 'age':9}
    zip([iterable, ...])                # 返回对应数组
        list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
        a = [1, 2, 3],  b = ["a", "b", "c"]
        z = zip(a, b)                   # 压缩：[(1, "a"), (2, "b"), (3, "c")]
        zip(*z)                         # 解压缩：[(1, 2, 3), ("a", "b", "c")]
    unicode(string, encoding, errors)   # 将字符串string转化为unicode形式，string为encoded string。

"""模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle----模块Moudle"""

# -- Python模块搜索路径:
"""
(1)程序的主目录    (2)PYTHONPATH目录 (3)标准链接库目录 (4)任何.pth文件的内容
"""

# -- 查看全部的模块搜索路径
import sys

sys.path

# -- 模块的使用代码
import module1, module2  # 导入module1 使用module1.printer()
from module1 import printer  # 导入module1中的printer变量 使用printer()
from module1 imoprt *  # 导入module1中的全部变量 使用不必添加module1前缀

# -- 重载模块reload: 这是一个内置函数 而不是一条语句
from imp import reload

reload(module)

# -- 模块的包导入:使用点号(.)而不是路径(dir1\dir2)进行导入
import dir1.dir2.mod  # d导入包(目录)dir1中的包dir2中的mod模块 此时dir1必须在Python可搜索路径中
from dir1.dir2.mod import *  # from语法的包导入

# -- __init__.py包文件:每个导入的包中都应该包含这么一个文件
"""
该文件可以为空
首次进行包导入时 该文件会自动执行
高级功能:在该文件中使用__all__列表来定义包(目录)以from*的形式导入时 需要导入什么
"""

# -- 包相对导入:使用点号(.) 只能使用from语句
from . import spam  # 导入当前目录下的spam模块（错误: 当前目录下的模块, 直接导入即可）
from .spam import name  # 导入当前目录下的spam模块的name属性（错误: 当前目录下的模块, 直接导入即可，不用加.）
from .. import spam  # 导入当前目录的父目录下的spam模块

# -- 包相对导入与普通导入的区别
from string import *  # 这里导入的string模块为sys.path路径上的 而不是本目录下的string模块(如果存在也不是)
from .string import *  # 这里导入的string模块为本目录下的(不存在则导入失败) 而不是sys.path路径上的

# -- 模块数据隐藏:最小化from*的破坏
_X  # 变量名前加下划线可以防止from*导入时该变量名被复制出去
__all__ = ['x', 'x1', 'x2']  # 使用__all__列表指定from*时复制出去的变量名(变量名在列表中为字符串形式)

# -- 可以使用__name__进行模块的单元测试:当模块为顶层执行文件时值为'__main__' 当模块被导入时为模块名
if __name__ == '__main__':
    doSomething
# 模块属性中还有其他属性，例如：
__doc__  # 模块的说明文档
__file__  # 模块文件的文件名，包括全路径
__name__  # 主文件或者被导入文件
__package__  # 模块所在的包

# -- import语句from语句的as扩展
import modulename as name
from modulename import attrname as name

# -- 得到模块属性的几种方法 假设为了得到name属性的值
M.name
M.__dict__['name']
sys.modules['M'].name
getattr(M, 'name')
































