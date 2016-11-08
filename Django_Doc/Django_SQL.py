# -*- coding: utf-8 -*-

# 进行原始的SQL查询¶
# 在模型查询API不够用的情况下，你可以使用原始的SQL语句。
# Django 提供两种方法使用原始SQL进行查询：
# 一种是使用Manager.raw()方法，进行原始查询并返回模型实例；
# 另一种是完全避开模型层，直接执行自定义的SQL语句。


'''
进行原始查询¶

raw() 管理器方法用于原始的SQL查询，并返回模型的实例：

Manager.raw(raw_query, params=None, translations=None)¶
这个方法执行原始的SQL查询，并返回一个django.db.models.query.RawQuerySet 实例。
这个RawQuerySet 实例可以像一般的查询集那样，通过迭代来提供对象实例。

class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
你可以像这样执行自定义的SQL语句：

           for p in Person.objects.raw('SELECT * FROM myapp_person'):
              print(p)
             John Smith
             Jane Jones

'''

# 将查询字段映射到模型字段¶
#
# raw()方法自动将查询字段映射到模型字段。
#
# 字段的顺序并不重要。 换句话说，下面两种查询的作用相同：
#
# >>> Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
# ...
# >>> Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
#




'''
索引访问¶

raw()方法支持索引访问，所以如果只需要第一条记录，可以这样写：

>>> first_person = Person.objects.raw('SELECT * FROM myapp_person')[0]
然而，索引和切片并不在数据库层面上进行操作。 如果数据库中有很多的Person对象，更加高效的方法是在SQL层面限制查询中结果的数量：

>>> first_person = Person.objects.raw('SELECT * FROM myapp_person LIMIT 1')[0]
'''























































































