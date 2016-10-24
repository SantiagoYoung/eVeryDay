# -*- coding: utf-8 -*-
'''
www.dannysite.com
'''


'''
    关于Django的MVC层
        Django紧紧地遵循MVC模式，可以称得上是一种MVC框架。
            @ M：数据存取部分， 由django数据库层处理;
            @ V：选择哪些数据要显示，以及怎样显示， 由视图和模板处理;
            @ C：根据用户输入委派视图的部分，由Django框架根据URLconf设置， 对给定URL调用适当的Python函数。
    由于C由框架自行处理，而Django里更关注的是模型（Model）、模板（Template)和视图(Views)，因此Django也被称为MTV框架。
    在MTV开发模式中：
            @ M：数据存取层。该层处理与数据相关的所有事务：如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。
            @ T：表现层。该层处理与表现相关的决定：如何在页面或其他类型文档中进行显示;
            @ V：业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。模型和模板之间的桥梁。
'''


'Start project'
# django-admin.py startproject myblog
# python manage.py runserver

'''
连接数据库

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
'''
# python manage.py makemigrations
# python manage.py migrate

'''
探寻 django-admin.py 和 manage.py 的奥秘
'''


'''第二篇：开启博客系统之旅'''

'''
美好的构想
一个好的产品要从一个好的构思开始，也就是说我们要真正明白想实现什么、要达到怎样的效果。当然，这里的例子并不能称得上是一个“美好的构想”。
仅仅包含以下基本的构思：
博客拥有标题、作者、正文及发布的时间等基本的元素。同时，一个博客还会隶属于一个分类，并可能包含一个或多个标签。
博客也可以有一个或多个评论，评论中要记录评论者的称呼、邮箱以及评论内容；
需要有一个“博客列表”页来呈现发布的博客。博客要按发布时间的倒叙来排列，
每个博客都要包含标题、作者、分类、发布时间的显示（年-月-日 时:分）及节选的正文内容（前 100 个字）。点击单独的博客可以进入其详情页；
需要有一个“详情”页来呈现完整的博客，包括标题、作者、分类、发布的时间、标签和完整的正文内容，并附加评论显示和发布功能。
'''
# python manage.py startapp blog

from django.db import models

class Blog(models.Model):
    title = models.CharField('title', max_length=12)






























