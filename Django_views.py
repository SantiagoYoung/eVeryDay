# -*- coding: utf-8 -*-


# URL调度器
'''
对于高质量的Web 应用来说，使用简洁、优雅的URL 模式是一个非常值得重视的细节。
Django 让你随心所欲设计你的URL，不受框架束缚。
'''
'''
为了给一个应用设计URL，你需要创建一个Python 模块，通常称为URLconf（URL configuration）。
这个模块是纯粹的Python 代码，包含URL 模式（简单的正则表达式）到Python 函数（你的视图）的简单映射。
映射可短可长，随便你。它可以引用其它的映射。而且，因为它是纯粹的Python 代码，它可以动态构造。
'''

# Django 如何处理一个请求
#urlpatterns 是 django.conf.urls.url() 实例的一个Python 列表。
'''
1. Django 决定要使用的根URLconf 模块。通常，这个值就是ROOT_URLCONF 的设置，
但是如果进来的HttpRequest 对象具有一个urlconf 属性（通过中间件request processing 设置），则使用这个值来替换ROOT_URLCONF 设置。
2. Django 加载该Python 模块并寻找可用的urlpatterns。它是django.conf.urls.url() 实例的一个Python 列表。
3. Django 依次匹配每个URL 模式，在与请求的URL 匹配的第一个模式停下来。
4. 一旦其中的一个正则表达式匹配上，Django 将导入并调用给出的视图，它是一个简单的Python 函数（或者一个基于类的视图）。
视图将获得如下参数:
    * 一个HttpRequest 实例。
    * 如果匹配的正则表达式返回了没有命名的组，那么正则表达式匹配的内容将作为位置参数提供给视图。
    * 关键字参数由正则表达式匹配的命名组组成，但是可以被django.conf.urls.url()的可选参数kwargs覆盖。
5. 如果没有匹配到正则表达式，或者如果过程中抛出一个异常，Django 将调用一个适当的错误处理视图。
请参见下面的错误处理。
'''


# from django.conf.urls import url
# from . import views
'''
urlpatterns =[
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
'''
# 命名组
# 在Python 正则表达式中，命名正则表达式组的语法是(?P<name>pattern)，其中name 是组的名称，pattern 是要匹配的模式。
'''
urlpatterns = [
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]
'''

# URLconf 在什么上查找
#
# 请求的URL被看做是一个普通的Python 字符串， URLconf在其上查找并匹配。进行匹配时将不包括GET或POST请求方式的参数以及域名。
#
# 例如，http://www.example.com/myapp/请求中，URLconf 将查找myapp/。
#
# 在http://www.example.com/myapp/?page=3 请求中，URLconf 仍将查找myapp/。
#
# URLconf 不检查使用了哪种请求方法。
# 换句话讲，所有的请求方法 —— 即，对同一个URL的无论是POST请求、GET请求、或HEAD请求方法等等 —— 都将路由到相同的函数。



# 捕获的参数都是字符串





# 指定视图参数的默认值
'''
有一个方便的小技巧是指定视图参数的默认值。 下面是一个URLconf 和视图的示例：

# URLconf
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...
在上面的例子中，两个URL模式指向同一个视图views.page —— 但是第一个模式不会从URL 中捕获任何值。
如果第一个模式匹配，page() 函数将使用num参数的默认值"1"。如果第二个模式匹配，page() 将使用正则表达式捕获的num 值。

'''



# 错误处理
'''
当Django 找不到一个匹配请求的URL 的正则表达式时，或者当抛出一个异常时，Django 将调用一个错误处理视图。

这些情况发生时使用的视图通过4个变量指定。它们的默认值应该满足大部分项目，但是通过赋值给它们以进一步的自定义也是可以的。

完整的细节请参见自定义错误视图。

这些值可以在你的根URLconf 中设置。在其它URLconf 中设置这些变量将不会产生效果。

它们的值必须是可调用的或者是表示视图的Python 完整导入路径的字符串，可以方便地调用它们来处理错误情况。

这些值是：

handler404 —— 参见django.conf.urls.handler404。
handler500 —— 参见django.conf.urls.handler500。
handler403 —— 参见django.conf.urls.handler403。
handler400 —— 参见django.conf.urls.handler400。
'''


# 嵌套的参数
'''
正则表达式允许嵌套参数，Django 将解析它们并传递给视图。
当反查时，Django 将尝试填满所有外围捕获的参数，并忽略嵌套捕获的参数。考虑下面的URL 模式，它带有一个可选的page 参数：

from django.conf.urls import url

urlpatterns = [
    url(r'blog/(page-(\d+)/)?$', blog_articles),                  # bad
    url(r'comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
]
两个模式都使用嵌套的参数，其解析方式是：例如blog/page-2/ 将匹配blog_articles并带有两个位置参数page-2/ 和2。
第二个comments 的模式将匹配comments/page-2/ 并带有一个值为2 的关键字参数page_number。这个例子中外围参数是一个不捕获的参数(?:...)。
'''


#传递额外的选项给视图函数
'''
URLconfs 具有一个钩子，让你传递一个Python 字典作为额外的参数传递给视图函数。

django.conf.urls.url() 函数可以接收一个可选的第三个参数，它是一个字典，表示想要传递给视图函数的额外关键字参数。

例如：

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
]
在这个例子中，对于/blog/2005/请求，Django 将调用views.year_archive(request, year='2005', foo='bar')
'''




# URL的反向解析
'''
要获取一个URL，最初拥有的信息是负责处理它的视图的标识（例如名字），与
查找正确的URL的其它必要的信息如视图参数的类型(位置参数、关键字参数）和值。


Django 提供了一个解决方案使得URL 映射是URL 设计唯一的储存库。你用你的URLconf填充它，然后可以双向使用它：
     * 根据用户/浏览器发起的URL 请求，它调用正确的Django 视图，并从URL 中提取它的参数需要的值。
     * 根据Django 视图的标识和将要传递给它的参数的值，获取与之关联的URL。
第一种方式是我们在前面的章节中一直讨论的用法。
第二种方式叫做反向解析URL、反向URL匹配、反向URL查询或者简单的URL反查。

在需要URL 的地方，对于不同层级，Django 提供不同的工具用于URL 反查：
在模板中：使用url 模板标签。
在Python 代码中：使用django.core.urlresolvers.reverse() 函数。
在更高层的与处理Django 模型实例相关的代码中：使用get_absolute_url() 方法。
'''



# URL  命名空间
'''
一个URL命名空间有两个部分， 它们都是字符串：
    应用命名空间： 表示正在部署的应用的名称。
    实例命名空间： 表示应用的一个特定的实例。
    URL的命名空间使用‘：’操作符指定。
'''


















