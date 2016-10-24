# -*- coding: utf-8 -*-
'''
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cses aren't special enough to break the rules.
9. Errors should never pass silently.
10. Unless explicitly silenced.
11. In the face of ambiguity, refuse the temptation to guess.
12. There should be one-- and preferbly only one --obvious way to do it.
13. Although that way may not be obvious at first unless you're Dutch.
14. Now is better than never.
15. Although never is often better than 'right' now.
16. If the implementation is hard to explain, it's  bad idea.
17. If the implementation is easy to explain, it may be a good idea.
18. Namespace are one honking great idea -- let's do more of those!
'''


import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print r.status_code
# print r.headers['content-type']
# print r.encoding
# print r.text
# print r.json()

'''
发送请求
'''
r = requests.get('https://github.com/timeline.json')
#  r 是一个Response对象.
print '1>', r.text

p = requests.post('http://httpbin.org/post')
print '2>', p.text

put = requests.put('http://httpbin.org/put')
print '3>', put.text

delete = requests.delete('http://httpbin.org/delete')
print '4>', delete.text

head = requests.head('http://httpbin.org/get')
print '5>', head.content

opt = requests.options('http://httpbin.org/get')
print '6>', opt.content

'''
传递URL参数
'''
payload = {'key': 'value1', 'key2': 'value2'}
py = requests.get('http://httpbin.org/get', params=payload)
print '7>', py.url
print '7>', py.text

pyload = {'key1': 'value1', 'key2': ['value2', 'value2']}
pl = requests.get('http://httpbin.org/get', params=pyload)
print '8>', pl.url
print '8>', pl.text

'''
响应内容
'''
bd = requests.get('https://www.baidu.com')
print '9>', bd.text
print '9>', bd.url
print '9>', bd.encoding



'''
二进制响应内容
'''
# resp = requests.get('https://github.com/timeline.json')
# import Image
# from io import BytesIO
# i = Image.open(BytesIO(resp.content))
# i.show()


'''
JSON响应内容
'''
respon = requests.get('https://github.com/timeline.json')
print '10>', respon.json()


'''
原始响应内容
'''
neon = requests.get('https://github.com/timeline.json', stream=True)
print '11>', neon.raw


'''
定制请求头
'''
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
non = requests.get(url, headers)
print '12>', non.headers


'''
更加复杂的POST请求
'''
pyload = {'key1': 'value1', 'key2': 'value2'}
nen = requests.post('http://httpbin.org/post', data=pyload)
print '13>', nen.text

import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(pyload))
print '14>', r.text


'''
响应状态码
'''
r = requests.get('http://httpbin.org/get')
print '15>', r.status_code
print '15>', r.status_code == requests.codes.ok
print '15>', r.raise_for_status()

# bad_r = requests.get('http://httpbin.org/status/404')
# print '16>', bad_r.status_code
# print '16>', bad_r.raise_for_status()



'''
Cookie
'''

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print '17', r
# print '17>', r.cookies['example_cookie_name']

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print '17>', r.text




'''
重定向与请求历史
'''
r = requests.get('http://github.com')
print '18>', r.url
print '18>', r.status_code
print '18>', r.history


r = requests.get('http://github.com', allow_redirects=False)
print '19', r.status_code
print '19', r.history



r = requests.head('http://github.com', allow_redirects=True)
print '20', r.url
print '20', r.history


'''
超时
注意
timeout 仅对连接过程有效，与响应体的下载无关。
timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常
 （更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
'''
r = requests.get('http://github.com', timeout=0.0001)
print '21>', r



'''
错误与异常

遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

若请求超时，则抛出一个 Timeout 异常。

若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
'''
