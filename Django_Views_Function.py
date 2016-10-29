# -*- coding: utf-8 -*-


# 编写视图

'''
一个视图函数，简称视图，是一个简单的Python 函数，
它接受Web请求并且返回Web响应。
响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片. . .
是任何东西都可以。
无论视图本身包含什么逻辑，都要返回响应。
代码写在哪里也无所谓，只要它在你的Python目录下面。
'''
from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

# 把你的URL映射到视图
# 所以，再重复一遍，这个视图函数返回了一个包含当前日期和时间的HTML页面。
# 你需要创建一个URLconf，以便使用特定的URL展示这一视图；

'''
返回错误
在Django中返回HTTP错误代码是相当容易的。
HttpResponse的许多子类对应着除了200（代表“OK”）以外的一些常用的HTTP状态码。
'''
from django.http import HttpResponse

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)



#Http404异常
'''
class django.http.Http404


当你返回一个像HttpResponseNotFound这样的错误时，它会输出这个错误页面的HTML作为结果：
return HttpResponseNotFound('<h1>Page not found</h1>')

为了便利起见，也因为你的站点有个一致的404页面是个好主意，Django提供了Http404异常。
如果你在视图函数中的任何地方抛出Http404异常，
Django都会捕获它，并且带上HTTP404错误码返回你应用的标准错误页面。
像这样：

from django.http import Http404
from django.shortcuts import render_to_response
from polls.models import Poll

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('polls/detail.html', {'poll': p})

为了尽可能利用 Http404，你应该创建一个用来在404错误产生时展示的模板。
这个模板应该叫做404.html，并且在你的模板树中位于最顶层。

如果你在抛出Http404异常时提供了一条消息，当DEBUG为True时它会出现在标准404模板的展示中。
你可以将这些消息用于调试；但他们通常不适用于404模板本身。
'''


#自定义错误视图

# handler404覆盖page_not_found()视图：
handler404 = 'mysite.views.my_custom_page_not_found_view'
# handler500覆盖server_error()视图：
handler500 = 'mysite.views.my_custom_error_view'
#handler403覆盖 permission_denied()视图：
handler403 = 'mysite.views.my_custom_permission_denied_view'
#handler400覆盖来bad_request()视图
handler400 = 'mysite.views.my_custom_bad_request_view'


# 配置
# 1.设置settings文件
#        DEBUG = False

# 2.配置urls文件
#       from django.conf.urls import handler400, handler500
#           handler404 = "login.views.page_not_found"
#           handler500 = "login.views.page_error"

# 3.在views文件中定义 page_not_found , page_error函数
#       from django.shortcuts import render_to_response
#           def page_not_found(request):
#               return render_to_response('404.html')
#           def page_error(request):
#               return render_to_response('500.html')

# 4.在app的templates下建立404.html和500.html文件



# Django shortcut functions

'''
The package django.shortcuts collects helper functions and
classes that 'span' multiple levels of MVC. In other words, these
functions/classes introduce controlled coupling for convenience's sake.
'''

#### render()
'''
render(request, template_name, context=None, content_type=None, status=None, using=None)
'''
# Required arguments :

'''
request: 用于生成response
template_name: 要使用的模板的完整名
'''
# optional arguments:
'''
context: 添加到模板上下文的一个字典。默认是一个空字典。
'''

####  render_to_response
'''
render_to_response(template_name[, context][, context_instance][, content_type][, status][, dirs][, using])
'''

# 必选的参数
#
# template_name

# 可选的参数
#
# context

# context_instance
# 渲染模板使用的上下文实例


##### redirect
'''
redirect(to, [permanent=False, ]*args, **kwargs)

为传递进来的参数返回HttpResponseRedirect 给正确的URL 。
参数可以是：

一个模型：将调用模型的get_absolute_url() 函数
一个视图，可以带有参数：将使用urlresolvers.reverse 来反向解析名称
一个绝对的或相对的URL，将原样作为重定向的位置。
默认返回一个临时的重定向；传递permanent=True 可以返回一个永久的重定向。
'''

#### get_object_or_404
'''
get_object_or_404(klass, *args, **kwargs)
在一个给定的模型管理器上调用get()，
但是引发Http404 而不是模型的DoesNotExist 异常。
'''

# 必选的参数¶

# klass
# 获取该对象的一个Model 类，Manager或QuerySet 实例。

# **kwargs
# 查询的参数，格式应该可以被get() 和filter()接受。


#### get_lit_or_404
'''
get_list_or_404(klass, *args, **kwargs)
返回一个给定模型管理器上filter() 的结果，
并将结果映射为一个列表，如果结果为空则返回Http404。
'''

#### 视图装饰器
# 限制HTTP的请求方法

#  require_http_methods(request_method_list)
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe

@require_http_methods(['GET','POST'])
def my_views(request):
    pass
# HTTP请求的方法名必须大写。

@require_POST()
@require_GET()
@require_safe()

















































