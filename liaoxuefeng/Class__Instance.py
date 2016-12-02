#  coding: utf-8

'''
面向对象最重要的概念就是 类(Class) 和 实例(Instance)。
 实例是根据类创建出来的一个个具体的 对象， 每个对象都拥有相同的方法， 但是各自的数据可能不同。

'''

# 仍以Student类为例，在Python中，定义类是通过class关键字：

class Student(object):
    pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
# 表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是
# 通过   类名+()   实现的：

bart = Student()
print bart
print Student

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：

bart.name = 'Bart simpson'
print bart.name

# 由于类可以起到模板的作用，
# 因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
# 必须传入与__init__方法匹配的参数，但self不需要传，

bart = Student('Bart Simpson', 59)
print bart.name
print bart.score

# 和普通的函数相比，在类中定义的函数只有一点不同，
# 就是第一个参数永远是实例变量self，并且，调用时，不用传递该参参数


# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '{}: {}'.format(self.name, self.score)

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。

bart = Student('Bart Simpson', 89)
lisa = Student('Lisa Simpson', 87)
bart.print_score()

# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '{}: {}'.format(self.name, self.score)


    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60 and self.score < 90:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 89)
print bart.get_grade()

bart.age = 14
print bart.__dict__









































