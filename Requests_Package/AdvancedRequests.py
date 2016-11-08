# -*- coding: utf-8 -*-

import requests


'''
会话对象
会话对象让你能够跨请求保持某些参数。
它也会在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。
所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
'''

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

r = s.get('http://httpbin.org/cookies')
print r.text
# '{"cookies": {"sessioncookie": "123456789"}}'



# 会话也可用来为请求方法提供缺省数据。这是通过为会话对象的属性提供数据来实现的：
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
# both 'x-test' and 'x-test2' are sent
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print 'santiago', r.headers
# 任何你传递给请求方法的字典都会与已设置会话层数据合并。方法层的参数覆盖会话的参数。


# 不过需要注意，就算使用了会话，方法级别的参数也不会被跨请求保持。
# 下面的例子只会和第一个请求发送 cookie ，而非第二个：
s = requests.Session()
r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print 'neon', r.text

r = s.get('http://httpbin.org/cookies')
print 'neon', r.text



# 请求与响应对象
# 任何时候调用 requests.*() 你都在做两件主要的事情。
# 其一，你在构建一个 Request 对象， 该对象将被发送到某个服务器请求或查询一些资源。
# 其二，一旦 requests 得到一个从 服务器返回的响应就会产生一个 Response 对象。
# 该响应对象包含服务器返回的所有信息， 也包含你原来创建的 Request 对象。

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
print '>>', r.headers
print '>>>', r.request.headers


# 准备的请求 （Prepared Request）
# 当你从 API 或者会话调用中收到一个 Response 对象时，request 属性其实是使用了 PreparedRequest。
# 有时在发送请求之前，你需要对 body 或者 header （或者别的什么东西）做一些额外处理，下面演示了一个简单的做法：
from requests import Request, Session
s = Session()
url ='www.baidu.com'
data = {'neon': 'god'}
headers = {'content-type': 'text/html'}
req = Request('GET', url,
              data=data,
              headers=headers)
prepared = req.prepare()
# do something with prepped.body
# do something with prepped.headers
stream = True
verify = True
proxies= None
cert = None
timeout = 1
resp = s.send(prepared,
              stream=stream,
              verify=verify,
              proxie=proxies,
              cert=cert,
              timeout=timeout)
print resp.status_code


# 然而，上述代码会失去 Requests Session 对象的一些优势，
# 尤其 Session 级别的状态，例如 cookie 就不会被应用到你的请求上去。
# 要获取一个带有状态的 PreparedRequest，
# 请用 Session.prepare_request() 取代 Request.prepare() 的调用，如下所示：


s = Session()
req = Request('GET', url, data=data, headers=headers)
prepared = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepared, stream=stream, verify=verify, proxies=proxies, cert=cert, timeout=timeout)

print resp.status_code



'''
SSL 证书验证
Requests 可以为 HTTPS 请求验证 SSL 证书，就像 web 浏览器一样。
要想检查某个主机的 SSL 证书，你可以使用 verify 参数:
'''

r = requests.get('https://kennethreitz.com', verify=True)


'''
响应体内容工作流
默认情况下，当你进行网络请求后，响应体会立即被下载。
你可以通过 stream 参数覆盖这个行为，推迟下载响应体直到访问 Response.content 属性：
'''
tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True)
# 此时仅有响应头被下载下来了，连接保持打开状态，因此允许我们根据条件获取内容：
if int(r.headers['content-length']) < 20:
    content = r.content
print content

# 你可以进一步使用 Response.iter_content 和 Response.iter_lines 方法来控制工作流，
# 或者以 Response.raw 从底层 urllib3 的 urllib3.HTTPResponse <urllib3.response.HTTPResponse 读取。


# 如果你在请求中把 stream 设为 True，Requests 无法将连接释放回连接池，除非你 消耗了所有的数据，
# 或者调用了 Response.close。 这样会带来连接效率低下的问题。
# 如果你发现你在使用 stream=True 的同时还在部分读取请求的 body（或者完全没有读取 body），
# 那么你就应该考虑使用 contextlib.closing (文档)， 如下所示：

from contextlib import closing

with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
    # 在此处理响应。




    # 保持活动状态（持久连接）¶
    #
    # 好消息——归功于
    # urllib3，同一会话内的持久连接是完全自动处理的！同一会话内你发出的任何请求都会自动复用恰当的连接！

    # 注意：只有所有的响应体数据被读取完毕连接才会被释放为连接池；
    # 所以确保将stream设置为False或读取Response对象的content属性。


    # 流式上传¶
    # Requests支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存。
    # 要使用流式上传，仅需为你的请求体提供一个类文件对象即可：
    with open('massive-body') as f:
        requests.post('http://some.url/streamed', data=f)
#
# 警告
# 我们强烈建议你用二进制模式（binary mode）打开文件。
# 这是因为 requests 可能会为你提供 header 中的 Content-Length，
# 在这种情况下该值会被设为文件的字节数。如果你用文本模式打开文件，就可能碰到错误。


# 块编码请求
# 对于出去和进来的请求，Requests 也支持分块传输编码。
# 要发送一个块编码的请求，仅需为你的请求体提供一个生成器（或任意没有具体长度的迭代器）：

def gen():
    yield 'hi'
    yield 'there'

requests.post('http://some.url/chunked', data=gen())

# 对于分块的编码请求，我们最好使用 Response.iter_content()
# 对其数据进行迭代。在理想情况下，你的 request 会设置 stream=True，
# 这样你就可以通过调用 iter_content 并将分块大小参数设为 None，
# 从而进行分块的迭代。如果你要设置分块的最大体积，你可以把分块大小参数设为任意整数。


# POST 多个分块编码的文件¶

# 你可以在一个请求中发送多个文件。例如，假设你要上传多个图像文件到一个 HTML 表单，
# 使用一个多文件 field 叫做 "images":
#
# <input type="file" name="images" multiple="true" required="true"/>

# 要实现，只要把文件设到一个元组的列表中，其中元组结构为 (form_field_name, file_info):

>>> url = 'http://httpbin.org/post'
>>> multiple_files = [
        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
>>> r = requests.post(url, files=multiple_files)
>>> r.text
{
  ...
  'files': {'images': 'data:image/png;base64,iVBORw ....'}
  'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
  ...
}



# # 事件挂钩
# Requests有一个钩子系统，你可以用来操控部分请求过程，或信号事件处理。
#
# 可用的钩子:
#
# response:
# 从一个请求产生的响应
# 你可以通过传递一个 {hook_name: callback_function} 字典给 hooks 请求参数 为每个请求分配一个钩子函数：
hooks = dict(response=print_url)

# callback_function 会接受一个数据块作为它的第一个参数。

def print_url(r, *args, **kwargs):
    print(r.url)
# 若执行你的回调函数期间发生错误，系统会给出一个警告。

import requests

def print_url(r, *args, **kwargs):
    print r.url

print requests.get('http://httpbin.org', hooks= dict(response=print_url))


# # 自定义身份验证¶
# Requests 允许你使用自己指定的身份验证机制。
#
# 任何传递给请求方法的 auth 参数的可调用对象，在请求发出之前都有机会修改请求。

# 自定义的身份验证机制是作为 requests.auth.AuthBase 的子类来实现的，也非常容易定义。
# Requests 在 requests.auth 中提供了两种常见的的身份验证方案： HTTPBasicAuth 和 HTTPDigestAuth 。

# 假设我们有一个web服务，仅在 X-Pizza 头被设置为一个密码值的情况下才会有响应。
# 虽然这不太可能，但就以它为例好了。

from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r
# 然后就可以使用我们的PizzaAuth来进行网络请求:

>>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
<Response [200]>



# 流式请求¶
#
# 使用 requests.Response.iter_lines() 你可以很方便地对流式 API （例如 Twitter 的流式 API ） 进行迭代。
# 简单地设置 stream 为 True 便可以使用 iter_lines() 对相应进行迭代：

import json
import requests

r = requests.get('http://httpbin.org/stream/20', stream=True)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        print(json.loads(line))

# 警告
# iter_lines() 不保证重进入时的安全性。多次调用该方法 会导致部分收到的数据丢失。
# 如果你要在多处调用它，就应该使用生成的迭代器对象:

lines = r.iter_lines()
# Save the first line for later or just skip it

first_line = next(lines)

for line in lines:
    print(line)



# 代理¶
# 如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求:

# 如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求:

import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)
# 你也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理。

$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"

$ python
>>> import requests
>>> requests.get("http://example.org")
# 若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/ 语法：

proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}
# 要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。

proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
# 注意，代理 URL 必须包含连接方式。


# SOCKS¶

2.10.0 新版功能.
#
# 除了基本的 HTTP 代理，Request 还支持 SOCKS 协议的代理。这是一个可选功能，若要使用， 你需要安装第三方库。
#
# 你可以用 pip 获取依赖:
#
# $ pip install requests[socks]
# 安装好依赖以后，使用 SOCKS 代理和使用 HTTP 代理一样简单：

proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}

# 编码方式
# 当你收到一个响应时，Requests 会猜测响应的编码方式，用于在你调用 Response.text 方法时对响应进行解码。
# Requests 首先在 HTTP 头部检测是否存在指定的编码方式，如果不存在，则会使用 charade 来尝试猜测编码方式。
#
# 只有当 HTTP 头部不存在明确指定的字符集，并且 Content-Type 头部字段包含 text 值之时，
# Requests 才不去猜测编码方式。在这种情况下， RFC 2616 指定默认字符集必须是 ISO-8859-1 。
# Requests 遵从这一规范。如果你需要一种不同的编码方式，你可以手动设置 Response.encoding 属性，
# 或使用原始的 Response.content。



# HTTP动词
# Requests 提供了几乎所有HTTP动词的功能：GET、OPTIONS、HEAD、POST、PUT、PATCH、DELETE。
# 以下内容为使用 Requests 中的这些动词以及 Github API 提供了详细示例。
#
# 我将从最常使用的动词 GET 开始。
# HTTP GET 是一个幂等方法，从给定的 URL 返回一个资源。因而，当你试图从一个 web 位置获取数据之时，你应该使用这个动词。一个使用示例是尝试从 Github 上获取关于一个特定 commit 的信息。
# 假设我们想获取Requests的commit a050faf 的信息。我们可以这样去做：




>>> import requests
>>> r = requests.get('https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
# 我们应该确认 GitHub 是否正确响应。
# 如果正确响应，我们想弄清响应内容是什么类型的。像这样去做：

>>> if (r.status_code == requests.codes.ok):
...     print r.headers['content-type']
...
application/json; charset=utf-8
# 可见，GitHub 返回了 JSON 数据，非常好，
# 这样就可以使用 r.json 方法把这个返回的数据解析成 Python 对象。

>>> commit_data = r.json()

>>> print commit_data.keys()
[u'committer', u'author', u'url', u'tree', u'sha', u'parents', u'message']

>>> print commit_data[u'committer']
{u'date': u'2012-05-10T11:10:50-07:00', u'email': u'me@kennethreitz.com', u'name': u'Kenneth Reitz'}

>>> print commit_data[u'message']
makin' history
# 到目前为止，一切都非常简单。嗯，我们来研究一下 GitHub 的 API。
# 我们可以去看看文档，但如果使用 Requests 来研究也许会更有意思一点。
# 我们可以借助 Requests 的 OPTIONS 动词来看看我们刚使用过的 url 支持哪些 HTTP 方法。

















































