# coding: utf-8

# 在OOP程序设计中，当我们定义一个class的时候，
# 可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。


class Animal(object):

    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    # pass
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat....'


class Cat(Animal):
    # pass
    def run(self):
        print 'Cat is running....'

# 继承有什么好处？最大的好处是子类获得了父类的全部功能。

dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个     好处：多态。



'''
  什么是多态？
  当我们定义一个class的时候， 我们实际上就定义的一种数据类型。
  我们定义的数据类型和Python自带的数据类型，如str、list、dict一样。
'''
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly....'
run_twice(Tortoise())

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，因此，传入的任意类型，
# 只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：













