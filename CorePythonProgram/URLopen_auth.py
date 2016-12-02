#!/usr/bin/env python
import urllib2





LOGIN = 'wesley'
PASSWD = "hello"
URL = 'http://localhost'
REALM = 'Secure Archive'

def handler_verision(url):
    from urlparse import urlparse
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urlparse(URL)[1],
                      LOGIN, PASSWD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url



if __name__ == '__main__':
    handler_verision(URL)