# -*- coding: utf-8 -*-
from django.db import models
# choice

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES =(
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophmore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    year_in_school = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN, max_length=1)
# get_year_in_shchool_display()
    def is_upperclas(self):

        return self.year_in_shchool in (self.JUNIOR, self.SENIOR, self.SOPHOMORE)


# ForeignKey.limit_choices_to
from django.contrib.auth.models import User

staff_member = models.ForeignKey(User, limit_choices_to={'is_staff': True})

import datetime
def limit_pub_date_choice():
    return {'pub_date__lte': datetime.date.utcnow()}
limit_choices_to = limit_pub_date_choice

# ForeignKey.related_name
# ForeignKey.related_query_name

user = models.ForeignKey(User, related_name='+')

article = models.ForeignKey(User,related_name='tags',related_query_name='tag')







'''
模型实例

要创建模型的一个新实例，只需要像其他Python类一样实例化它

class Model(**kwargs)
关键字参数就是你的模型中定义的字段的名称。
保存实例化后的数据，你需要调用save().
'''
# 1.  增加类方法
class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)

        return book
book = Book.create('Pride and Prejudice')

# 2. 在自定义管理器中添加方法
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        return book
class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

book = Book.objects.create_book('Pride and Prejudice')


'''
自定义化模型加载
classmethod Model.from_db(db, firld_names, values)
from_db() 方法用于子模型从数据库加载时自定义模型实例。
db 参数包含数据库的别名，field_names 包含所有加载的字段的名称，values 包含field_names 中每个字段加载的值。
field_names 与values 的顺序相同，所以可以使用cls(**(zip(field_names, values))) 来实例化对象。
如果模型的所有字段都提供， values 需要被保证其顺序与__init__() 所期望的一致。这表示此时实例可以通过cls(*values) 创建。
可以通过cls._deferred 来检查是否提供所有的字段 —— 如果为 False，那么所有的字段都已经从数据库中加载。
此外为了创建新模型，from_db() 方法必须在新实例的属性_state 中设置adding 和 db 标识。
'''
# @classmethod
# def from_db(cls, db, field_names, values):
#
#     if cls._deferred:
#         instance = cls(**zip(field_names, values))
#     else:
#         instance = cls(*values)
#     instance._state.adding = False
#     instance._state.db = db
#
#     instance._loaded_values = zip(field_names, values)
#
# def save(self, *args, **kwargs):
#     if not self._state.adding and (self.creator_id != self._loaded_values['creator_id']):
#         raise ValueError(' no no no ')
#     super(..).save(*args, **kwargs)


'''
验证对象
验证一个模型涉及三个步骤：

1. 验证模型的字段 —— Model.clean_fields()
2. 验证模型的完整性 —— Model.clean()
3. 验证模型的唯一性 —— Model.validate_unique()
当你调用模型的full_clean() 方法时，这三个方法都将执行。

当你使用ModelForm时，is_valid() 将为表单中的所有字段执行这些验证。更多信息参见ModelForm 文档。
如果你计划自己处理验证出现的错误，或者你已经将需要验证的字段从ModelForm 中去除掉，你只需调用模型的full_clean() 方法。
Model.full_clean(exclude=None, validate_unique=True)¶
该方法按顺序调用Model.clean_fields()、Model.clean() 和Model.validate_unique()（如果validate_unique 为True），
并引发一个ValidationError，该异常的message_dict 属性包含三个步骤的所有错误。
可选的exclude 参数用来提供一个可以从验证和清除中排除的字段名称的列表。
ModelForm 使用这个参数来排除表单中没有出现的字段，使它们不需要验证，因为用户无法修正这些字段的错误。
注意，当你调用模型的save() 方法时，full_clean() 不会 自动调用。如果你想一步就可以为你手工创建的模型运行验证，你需要手工调用它。
例如：
'''
# from django.core.exceptions import  ValidationError
# try:
#     article.full_clean()
# except ValidationError as e:
#     pass

'''
full_clean() 第一步执行的是验证每个字段。
Model.clean_fields(exclude=None)¶
这个方法将验证模型的所有字段。可选的exclude 参数让你提供一个字段名称列表来从验证中排除。如果有字段验证失败，它将引发一个ValidationError。

full_clean() 第二步执行的是调用Model.clean()。如要实现模型自定义的验证，应该覆盖这个方法。
Model.clean()
应该用这个方法来提供自定义的模型验证，以及修改模型的属性。
例如，你可以使用它来给一个字段自动提供值，或者用于多个字段需要一起验证的情形：
'''
import datetime
from django.core.exceptions import ValidationError
from django.db import models
class Article(models.Model):

    def clean(self):
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Draft nooo')
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()

'''
Model.validate_unique(exclude=None)¶
该方法与clean_fields() 类似，只是验证的是模型的所有唯一性约束而不是单个字段的值。
可选的exclude 参数允许你提供一个字段名称的列表来从验证中排除。如果有字段验证失败，将引发一个 ValidationError。
注意，如果你提供一个exclude 参数给validate_unique()，任何涉及到其中一个字段的unique_together 约束将不检查。
'''


# 对象保存
# 默认情况下每个模型都有一个AutoField 叫做id，除非你显式指定模型某个字段的 primary_key=True。

'''
pk 属性

Model.pk
无论你是自己定义还是让Django 为你提供一个主键字段， 每个模型都将具有一个属性叫做pk。
它的行为类似模型的一个普通属性，但实际上是模型主键字段属性的别名。
你可以读取并设置它的值，就和其它属性一样，它会更新模型中正确的值。


显式指定自增主键的值

如果模型具有一个AutoField，但是你想在保存时显式定义一个新的对象ID，你只需要在保存之前显式指定它而不用依赖ID 自动分配的值：
>>> b3 = Blog(id=3, name='Cheddar Talk', tagline='Thoughts on cheese.')
>>> b3.id     # Returns 3.
>>> b3.save()
>>> b3.id     # Returns 3.
如果你手工赋值一个自增主键的值，请确保不要使用一个已经存在的主键值！
如果你使用数据库中已经存在的主键值创建一个新的对象，Django 将假设你正在修改这个已存在的记录而不是创建一个新的记录。

接着上面的'Cheddar Talk' 博客示例，下面这个例子将覆盖数据库中之前的记录：

b4 = Blog(id=3, name='Not Cheddar', tagline='Anything but cheese.')
b4.save()  # Overrides the previous blog with ID=3!
出现这种情况的原因，请参见下面的Django 如何知道是UPDATE 还是INSERT。

显式指定自增主键的值对于批量保存对象最有用，但你必须有信心不会有主键冲突。
'''

# 当你保存是，发生来什么？
'''
当你保存一个对象时，Django 执行以下步骤：

发出一个pre-save 信号。 发送一个django.db.models.signals.pre_save 信号，以允许监听该信号的函数完成一些自定义的动作。

预处理数据。 如果需要，对对象的每个字段进行自动转换。

大部分字段不需要预处理 —— 字段的数据将保持原样。预处理只用于具有特殊行为的字段。
例如，如果你的模型具有一个auto_now=True 的DateField，那么预处理阶段将修改对象中的数据以确保该日期字段包含当前的时间戳。
（我们的文档还没有所有具有这种“特殊行为”字段的一个列表。）

准备数据库数据。 要求每个字段提供的当前值是能够写入到数据库中的类型。

大部分字段不需要数据准备。简单的数据类型，例如整数和字符串，是可以直接写入的Python 对象。
但是，复杂的数据类型通常需要一些改动。

例如，DateField 字段使用Python 的 datetime 对象来保存数据。
数据库保存的不是datetime 对象，所以该字段的值必须转换成ISO兼容的日期字符串才能插入到数据库中。

插入数据到数据库中。 将预处理过、准备好的数据组织成一个SQL 语句用于插入数据库。

发出一个post-save 信号。 发送一个django.db.models.signals.post_save 信号，以允许监听听信号的函数完成一些自定义的动作。

'''


# get_absolute_url

# get_absolute_url() 方法告诉Django 如何计算对象的标准URL。
# 对于调用者，该方法返回的字符串应该可以通过HTTP 引用到这个对象。
def get_absolute_url(self):
    return "/people/%i/" % self.id
'''
（虽然这段代码又正确又简单，但这并不是让该方法满足可移植性的最好方式。
使get_absolute_url()函数满足可移植性的最好方式，通常是使用reverse() 函数。）

例如：
'''
def get_absolute_url(self):
    from django.core.urlresolvers import reverse
    return reverse('people.views.details', args=[str(self.id)])





## 关联对象参考
'''
class RelatedManager
"关联管理器"是在一对多或者多对多的关联上下文中使用的管理器。它存在于下面两种情况：
1. ForeignKey关系的“另一边”。像这样：
from django.db import models

class Reporter(models.Model):
    # ...
    pass

class Article(models.Model):
    reporter = models.ForeignKey(Reporter)
在上面的例子中，管理器可以使用reporter.article_set方法。

2. ManyToManyField关系的两边：

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
这个例子中，管理器将会拥有topping.pizza_set 和pizza.toppings两个方法。
'''

# add(obj1[,obj2,..])
# >>> b = Blog.objects.get(id=1)
# >>> e = Entry.objects.get(id=234)
# >>> b.entry_set.add(e) # Associates Entry e with Blog b.


# create(**kwargs)
# >>> b = Blog.objects.get(id=1)
# >>> e = b.entry_set.create(
# ...     headline='Hello',
# ...     body_text='Hi',
# ...     pub_date=datetime.date(2005, 1, 1)
# ... )
#
# # No need to call e.save() at this point -- it's already been saved.


# remove(obj1[,obj2,..])
# >>> b = Blog.objects.get(id=1)
# >>> e = Entry.objects.get(id=234)
# >>> b.entry_set.remove(e) # Disassociates Entry e from Blog b.



# clear()
# 从关联对象集中移除一切对象。
#
# >>> b = Blog.objects.get(id=1)
# >>> b.entry_set.clear()
# 就像 remove() 方法一样，clear()只能在 null=True的ForeignKey上被调用，也可以接受bulk关键词参数。























