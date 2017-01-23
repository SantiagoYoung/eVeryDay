
class Animal(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print 'Hello, I am %s.' % self.name

class Dog(Animal):

	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.a = 1
		self.b = 2
		self.c = 3

	def greet(self):
		super(Dog, self).greet()
		print 'wangwang...'



# dog = Dog('l')
# dog.greet()





class Base(object):
	def __init__(self):
		print 'enter Base'
		print 'leave Base'

class A(Base):
	def __init__(self):
		print 'enter A'
		super(A, self).__init__()
		print 'leave A'
class B(Base):
	def __init__(self):
		print 'enter B'
		super(B, self).__init__()
		print 'leave B'
class C(A, B):
	def __init__(self):
		print 'enter C'
		super(C, self).__init__()
		print 'leave C'


# c = C()

class Singleton(object):

	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			orig = super(Singleton, cls)
			cls._instance = orig.__new__(cls, *args, **kw)
		return cls._instance

class MyClass(Singleton):
	a = 1

one = MyClass()
two = MyClass()
print one.a
print two.a
print one.__dict__
print two.__dict__
print MyClass.__dict__
# print Singleton.__dict__
print one._instance
print MyClass._instance
print '*' * 60
print one
print two
print MyClass