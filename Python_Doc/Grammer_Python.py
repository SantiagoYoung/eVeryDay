# -*- coding: utf-8 -*-

"""语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句"""



#-- 赋值语句的形式
    spam = 'spam'                          # 基本形式
    spam, ham = 'spam', 'ham'              # 元组赋值形式
    [spam, ham] = ['s', 'h']               # 列表赋值形式
    a, b, c, d = 'abcd'                    # 序列赋值形式
    a, *b, c = 'spam'                      # 序列解包形式（Python3.x中才有）
    spam = ham = 'no'                      # 多目标赋值运算，涉及到共享引用
    spam += 42                             # 增强赋值，涉及到共享引用



#-- 序列赋值 序列解包
    [a, b, c] = (1, 2, 3)                  # a = 1, b = 2, c = 3
    a, b, c, d = "spam"                    # a = 's', b = 'p'
    a, b, c = range(3)                     # a = 0, b = 1
    a, *b = [1, 2, 3, 4]                   # a = 1, b = [2, 3, 4]
    *a, b = [1, 2, 3, 4]                   # a = [1, 2, 3], b = 4
    a, *b, c = [1, 2, 3, 4]                # a = 1, b = [2, 3], c = 4
    # 带有*时 会优先匹配*之外的变量 如
    a, *b, c = [1, 2]                      # a = 1, c = 2, b = []


#-- print函数原型
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    # 流的重定向
    print('hello world')                   # 等于sys.stdout.write('hello world')
    temp = sys.stdout                      # 原有流的保存
    sys.stdout = open('log.log', 'a')      # 流的重定向
    print('hello world')                   # 写入到文件log.log
    sys.stdout.close()
    sys.stdout = temp                      # 原有流的复原


#-- Python中and或or总是返回对象(左边的对象或右边的对象) 且具有短路求值的特性
    1 or 2 or 3                            # 返回 1
    1 and 2 and 3                          # 返回 3


#-- if/else三元表达符（if语句在行内）
    A = 1 if X else 2
    A = 1 if X else (2 if Y else 3)
    # 也可以使用and-or语句（一条语句实现多个if-else）
    result = (a > 20 and "big than 20" or a > 10 and "big than 10" or a > 5 and "big than 5")



#-- Python的while语句或者for语句可以带else语句 当然也可以带continue/break/pass语句
    while a > 1:
        anything
    else:
        anything
    # else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
    for i in range(5):
        anything
    else:
        anything

#-- 列表解析语法
    M = [[1,2,3], [4,5,6], [7,8,9]]
    res = [sum(row) for row in M]                     # G = [6, 15, 24] 一般的列表解析 生成一个列表
    res = [c * 2 for c in 'spam']                     # ['ss', 'pp', 'aa', 'mm']
    res = [a * b for a in [1, 2] for b in [4, 5]]     # 多解析过程 返回[4, 5, 8, 10]
    res = [a for a in [1, 2, 3] if a < 2]             # 带判断条件的解析过程
    res = [a if a > 0 else 0 for a in [-1, 0, 1]]     # 带判断条件的高级解析过程

# 两个列表同时解析：使用zip函数
for teama, teamb in zip(["Packers", "49ers"], ["Ravens", "Patriots"]):
    print(teama + " vs. " + teamb)
# 带索引的列表解析：使用enumerate函数
for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]):
    print(index, team)  # 输出0, Packers \n 1, 49ers \n ......



#-- 生成器表达式
    G = (sum(row) for row in M)                       # 使用小括号可以创建所需结果的生成器generator object
    next(G), next(G), next(G)                         # 输出(6, 15, 24)
    G = {sum(row) for row in M}                       # G = {6, 15, 24} 解析语法还可以生成集合和字典
    G = {i:sum(M[i]) for i in range(3)}               # G = {0: 6, 1: 15, 2: 24}



#-- 文档字符串:出现在Module的开端以及其中函数或类的开端 使用三重引号字符串


"""
    module document
    """
    def func():
        """
        function document
        """
        print()
    class Employee:
        """
        class document
        """
        print()
    print(func.__doc__)                # 输出函数文档字符串
    print(Employee.__doc__)            # 输出类的文档字符串

#-- 命名惯例:
    """
    以单一下划线开头的变量名(_X)不会被from module import*等语句导入
    前后有两个下划线的变量名(__X__)是系统定义的变量名，对解释器有特殊意义
    以两个下划线开头但不以下划线结尾的变量名(__X)是类的本地(私有)变量
    """
#-- 列表解析 in成员关系测试 map sorted zip enumerate内置函数等都使用了迭代协议
    'first line' in open('test.txt')   # in测试 返回True或False
    list(map(str.upper, open('t')))    # map内置函数
    sorted(iter([2, 5, 8, 3, 1]))      # sorted内置函数
    list(zip([1, 2], [3, 4]))          # zip内置函数 [(1, 3), (2, 4)]


#-- del语句: 手动删除某个变量
    del X

#-- 获取列表的子表的方法:
    x = [1,2,3,4,5,6]
    x[:3]                              # 前3个[1,2,3]
    x[1:5]                             # 中间4个[2,3,4,5]
    x[-3:]                             # 最后3个[4,5,6]
    x[::2]                             # 奇数项[1,3,5]
    x[1::2]                            # 偶数项[2,4,6]




#-- 手动迭代：iter和next
    L = [1, 2]
    I = iter(L)                        # I为L的迭代器
    I.next()                           # 返回1
    I.next()                           # 返回2
    I.next()                           # Error:StopIteration


#-- Python中的可迭代对象
    """
    1.range迭代器
    2.map、zip和filter迭代器
    3.字典视图迭代器：D.keys()), D.items()等
    4.文件类型
    """




















































