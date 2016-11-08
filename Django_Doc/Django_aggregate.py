# -*- coding: utf-8 -*-
# 聚合¶
# Django 数据库抽象API 描述了使用Django 查询来增删查改单个对象的方法。
# 然而，有时候你需要获取的值需要根据一组对象聚合后才能得到。
# 这份指南描述通过Django 查询来生成和返回聚合值的方法。
#
# 整篇指南我们都将引用以下模型。这些模型用来记录多个网上书店的库存。

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()



#Total number of books.
>>> Book.objects.count()

#Total number of books with publisher=BalonePress
Book.objects.filter(publisher__name='BalonePress').count()

# Average price across all books.
from django.db.models import Avg
Book.objects.all().aggregate(Avg('price'))

# Max price across all books.
>>> from django.db.models import Max
>>> Book.objects.all().aggregate(Max('price'))
{'price__max': Decimal('81.20')}



# Cost per page
>>> Book.objects.all().aggregate(
...    price_per_page=Sum(F('price')/F('pages'), output_field=FloatField()))
{'price_per_page': 0.4470664529184653}



>>> from django.db.models import Count
>>> pubs = Publisher.objects.annotate(num_books=Count('book'))
>>> pubs
[<Publisher BaloneyPress>, <Publisher SalamiPress>, ...]
>>> pubs[0].num_books
73

# The top 5 publishers, in order by number of books.
>>> pubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]
>>> pubs[0].num_books
1323



在查询集上生成聚合¶

Django提供了两种生成聚合的方法。第一种方法是从整个查询集生成统计值。比如，你想要计算所有在售书的平均价钱。Django的查询语法提供了一种方式描述所有图书的集合。

>>> Book.objects.all()
我们需要在QuerySet.对象上计算出总价格。这可以通过在QuerySet后面附加aggregate() 子句来完成。

>>> from django.db.models import Avg
>>> Book.objects.all().aggregate(Avg('price'))
{'price__avg': 34.35}
all()在这里是多余的，所以可以简化为：

>>> Book.objects.aggregate(Avg('price'))
{'price__avg': 34.35}




aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。
键的名称是聚合值的标识符，值是计算出来的聚合值。
键的名称是按照字段和聚合函数的名称自动生成出来的。
如果你想要为聚合值指定一个名称，可以向聚合子句提供它。

>>> Book.objects.aggregate(average_price=Avg('price'))
{'average_price': 34.35}



如果你希望生成不止一个聚合，你可以向aggregate()子句中添加另一个参数。
所以，如果你也想知道所有图书价格的最大值和最小值，可以这样查询：

>>> from django.db.models import Avg, Max, Min
>>> Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
{'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}




为查询集的每一项生成聚合¶

生成汇总值的第二种方法，是为QuerySet中每一个对象都生成一个独立的汇总值。
比如，如果你在检索一列图书，你可能想知道每一本书有多少作者参与。
每本书和作者是多对多的关系。我们想要汇总QuerySet.中每本书里的这种关系。

逐个对象的汇总结果可以由annotate()子句生成。
当annotate()子句被指定之后，QuerySet中的每个对象都会被注上特定的值。



这些注解的语法都和aggregate()子句所使用的相同。
annotate()的每个参数都描述了将要被计算的聚合。
比如，给图书添加作者数量的注解：

# Build an annotated queryset
>>> from django.db.models import Count
>>> q = Book.objects.annotate(Count('authors'))
# Interrogate the first object in the queryset
>>> q[0]
<Book: The Definitive Guide to Django>
>>> q[0].authors__count
2
# Interrogate the second object in the queryset
>>> q[1]
<Book: Practical Django Projects>
>>> q[1].authors__count
1




和使用 aggregate()一样，注解的名称也根据聚合函数的名称和聚合字段的名称得到的。
你可以在指定注解时，为默认名称提供一个别名：

>>> q = Book.objects.annotate(num_authors=Count('authors'))
>>> q[0].num_authors
2
>>> q[1].num_authors
1

与 aggregate() 不同的是， annotate() 不是一个终止子句。
annotate()子句的返回结果是一个查询集 (QuerySet)；
这个 QuerySet可以用任何QuerySet方法进行修改，包括 filter(), order_by(),
甚至是再次应用annotate()。



# 连接和聚合¶

至此，我们已经了解了作用于单种模型实例的聚合操作，
但是有时，你也想对所查询对象的关联对象进行聚合。

在聚合函数中指定聚合字段时，Django 允许你使用同样的 双下划线 表示关联关系，
然后 Django 在就会处理要读取的关联表，并得到关联对象的聚合。

例如，要得到每个书店的价格区别，可以使用如下注解：

>>> from django.db.models import Max, Min
>>> Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
这段代码告诉 Django 获取书店模型，并连接(通过多对多关系)图书模型，
然后对每本书的价格进行聚合，得出最小值和最大值。

同样的规则也用于  aggregate() 子句。
如果你想知道所有书店中最便宜的书和最贵的书价格分别是多少：

>>> Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
关系链可以按你的要求一直延伸。
例如，想得到所有作者当中最小的年龄是多少，就可以这样写：

>>> Store.objects.aggregate(youngest_age=Min('books__authors__age'))



s

annotate() 和filter() 子句的顺序¶
编写一个包含 annotate() 和 filter()  子句的复杂查询时，
要特别注意作用于 QuerySet的子句的顺序。

当一个annotate() 子句作用于某个查询时，
要根据查询的状态才能得出注解值，而状态由 annotate() 位置所决定。
以这就导致filter() 和 annotate() 不能交换顺序，下面两个查询就是不同的：

>>> Publisher.objects.annotate(num_books=Count('book')).filter(book__rating__gt=3.0)

另一个查询：
>>> Publisher.objects.filter(book__rating__gt=3.0).annotate(num_books=Count('book'))












































class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()