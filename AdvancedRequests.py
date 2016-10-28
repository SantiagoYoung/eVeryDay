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
if int(r.headers['content-length']) < 20:
    content = r.content
print content










































































