# -*- coding: utf-8 -*-

'''
Object Oriented Programming. OOP.

OOP 把对象作为程序的基本单元， 一个对象包含了数据和操作数据的函数。

面向对象的程序设计把计算机程序视为一组对象的集合， 而每个对象都可以接受其他对象发过来的消息，
并处理这些信息，计算机程序的执行就是一系列消息子各个对象之间的传递。


'''

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。

std1 = {'name': 'Michel', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}
def print_score(std):
    print '{0}: {1}'.format(std['name'], std['score'])



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '{}: {}'.format(self.name, self.score)

bart = Student('Bart Simpson', 89)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，
# 类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，
# 而实例（Instance）则是一个个具体的Student，
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student：
#
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
































































