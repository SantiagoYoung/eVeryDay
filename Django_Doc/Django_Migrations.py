# -*- coding: utf-8 -*-
#  迁移 Migrations

'''
迁移是Django用于同步你的发生改变的模型(添加一个字段，删除一个模型，等等。) 到你的数据库。
它的设计是很智能的, 但是你还是需要了解什么时候进行迁移, 什么时候去启动它们, 以及可能遇到的指令问题。
'''

# syncdb

#命令集
'''
@ migrate   负责执行迁移, 以及撤销和列出迁移的状态.
@ makemigrations  负责基于你的模板修改创建一个新的迁移.
@ sqlmigrate  展示迁移的sql语句.


你可以想象 migrations相当一个你的数据库的一个版本控制系统。
makemigrations 命令负责保存你的模型变化到一个迁移文件 - 和 commits很类似 - 同时 migrate负责将改变提交到数据库。
每个app 的迁移文件会保存到每个相应app的“migrations”文件夹里面,并且准备如何去执行它, 作为一个分布式代码库。
Django 将迁移你对模型和字段做出的任何改变 - 甚至包括那些对数据库没有影响的操作，
-在历史记录存放所有改变是正确重建field的唯一方式，你可能会在以后的数据迁移中使用到这些选项
（比如，在你定制了校验器的时候）。
'''
#工作流程
'''
迁移工作很简单。 修改你的模型
-比如添加字段和移除一个模型
- 然后运行 makemigrations:
'''


#迁移文件
'''
Migrations are stored as an on-disk format,
referred to here as “migration files”.
These files are actually just normal Python files with an agreed-upon object layout,
written in a declarative style.

A basic migration file looks like this:
'''
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [('migrations', '0001_initial')]
    operations = [
        migrations.DeleteModel('Tribble'),
        migrations.AddField('Author', 'rating',
                            models.IntegerField(default=0)),
    ]

'''
What Django looks for when it loads a migration file (as a Python module) is a subclass of django.db.migrations.
Migration called Migration. It then inspects this object for four attributes, only two of which are used most of the time:
    1. ependencies, a list of migrations this one depends on.
    2. operations, a list of Operation classes that define what this migration does.
'''

#Adding migrations to apps¶
'''
Adding migrations to new apps is straightforward -
they come preconfigured to accept migrations, and so just run makemigrations once you’ve made some changes.
If your app already has models and database tables,
 and doesn’t have migrations yet (for example, you created it against a previous Django version),
 you’ll need to convert it to use migrations; this is a simple process:
'''

#  $ python manage.py makemigrations your_app_label
# Now, run python manage.py migrate --fake-initial,
# and Django will detect that you have an initial migration
# and that the tables it wants to create already exist,
# and will mark the migration as already applied.



































































