# -*- coding: utf-8 -*-

'''

HTML 表单¶

在HTML中，表单是<form>...</form> 之间元素的集合，
它们允许访问者输入文本、选择选项、操作对象和控制等等，然后将信息发送回服务器。

某些表单的元素 —— 文本输入和复选框 —— 非常简单而且内建于HTML 本身。
其它的表单会复杂些；例如弹出一个日期选择对话框的界面、
允许你移动滚动条的界面、
使用JavaScript 和CSS 以及HTML 表单<input> 元素来实现操作控制的界面。

与<input> 元素一样，一个表单必须指定两样东西：

目的：响应用户输入的URL
方式：HTTP 方法
例如，Django Admin 站点的登录表单包含几个<input> 元素：
type="text" 用于用户名，
type="password" 用于密码，
type="submit" 用于“Log in" 按钮。它
还包含一些用户看不到的隐藏的文本字段，Django 使用它们来决定下一步的行为。

它还告诉浏览器表单数据应该发往<form> 的action 属性指定的URL —— /admin/，
而且应该使用method 属性指定的HTTP 方法 —— post。

当触发<input type="submit" value="Log in"> 元素时，数据将发送给/admin/。
'''


'''
GET 和 POST¶

处理表单时候只会用到GET 和 POST 方法。

Django 的登录表单使用POST 方法，
在这个方法中浏览器组合表单数据、
对它们进行编码以用于传输、
将它们发送到服务器然后接收它的响应。

相反，GET 组合提交的数据为一个字符串，
然后使用它来生成一个URL。
这个URL 将包含数据发送的地址以及数据的键和值。
如果你在Django 文档中做一次搜索，
你会立即看到这点，
此时将生成一个https://docs.djangoproject.com/search/?q=forms&release=1 形式的URL。
'''

# 用于改变系统状态的请求 —— 例如，给数据库带来变化的请求 —— 应该使用POST。
# GET 只应该用于不会影响系统状态的请求。






























