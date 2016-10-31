# -*- coding: utf-8 -*-



# class Manager
# 管理器是Django 的模型进行数据库查询操作的接口。Django 应用的每个模型都拥有至少一个管理器。

# 管理器的名字¶
'''
默认情况下，Django 为每个模型类添加一个名为objects的管理器。
然而，如果你想将objects用于字段名称，
或者你想使用其它名称而不是objects访问管理器，
你可以在每个模型类中重命名它们。在模型中定义一个值为models.Manager()的属性，来重命名管理器。
例如：
'''
from django.db import models
class Person(models.Model):
    people = models.Manager()
# 使用例子中的模型， Person.objects会抛出AttributeError异常，
# 而Person.people.all()会返回一个包含所有Person对象的列表。

#自定义管理器¶
'''
你可以在模型中使用自定义的管理器，方法是继承Manager 基类并实例化你的自定义管理器。

你有两个原因可能会自己定义管理器：
1. 向管理器类中添加额外的方法，
2. 或者修改管理器返回的原始查询集。
'''

# 添加额外的管理器方法¶
'''
添加额外管理器方法是为你的类增加“表级”功能的首选方式。
（如果要添加行级功能 —— 比如只对某个模型的实例起作用 ——应 使用模型方法 ，而不是管理器方法。）
'''
# 自定义的管理器 方法可以返回你想要的任何数据，而不需要返回一个查询集。
'''
例如，下面这个自定义管理器提供一个with_counts() 方法，
它返回所有OpinionPoll 对象的列表，
列表的每项都有一额外num_responses 属性，
该属性保存一个聚合查询的结果（注：对应的应是SQL查询语句中的COUNT（*）生成的项）：
'''
from django.db import models
class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        cursor = connection.cursor()
        # cursor.execute('''
        # SELECT p.id, p.question, p.poll_date, COUNT(*)
        # FROM  polls_opinionpoll p, polls_response r
        # WHERE p.id = r.poll_id
        # GROUP BY p.id, p.question, p.poll_date
        # ORDER BY p.poll_date DESC ''')
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id=row[0], question=row[1], poll_date=row[2])
            p.num_responses = row[3]
            result_list.append(p)
        return result_list
class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    poll_date = models.DateTimeField()
    objects = PollManager()


# 修改管理器的原始查询集¶

# 管理器自带的 查询集返回系统中所有的对象。例如，使用下面这个模型：
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

# Book.objects.all()语句将返回数据库中所有的Book对象。

'''
你可以通过重写Manager.get_queryset() 方法来覆盖管理器自带的Queryset。
get_queryset() 会根据你所需要的属性返回查询集。
'''


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager,self).get_queryset().filter(author='Roald Dahl')

class BBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager()
    dahl_objects  = DahlBookManager()

# 在这个简单的例子中，Book.objects.all()将返回数据库中所有的图书。
# 而 Book.dahl_objects.all() 只返回作者是 Roald Dahl 的图书。


# Of course, because get_queryset() returns a QuerySet object,
# you can use filter(), exclude() and all the other QuerySet methods on it.


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super(EditorManager, self).get_queryset().filter(role='E')

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    role = models.CharField(max_length=1,choices=(('A',_('Author')),('E', _('Editor'))))
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()


#
# 默认管理器¶
# 如果你使用自定义的管理器对象，要注意Django 遇到的第一个管理器（按照在模型中出现的顺序）拥有特殊的地位。
# Django 将类中定义的第一个管理器解释为默认的管理器，并且Django 中有几部分（包括dumpdata）将只使用该管理器。
# 因此，选择默认的管理器要小心谨慎仔细考量，这样才能避免因重写 get_queryset() 而可能产生的无法获取到预期数据的问题。



# 自定义管理器和模型继承¶
























