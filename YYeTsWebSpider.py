import urllib2
from bs4 import BeautifulSoup
import os


baseUrl = 'http://cili17.com/?_=123'

req = urllib2.Request(baseUrl)
response = urllib2.urlopen(req)
print response.read()

x = 'this is a test msg'
f = open('yyRes.json', 'w')
f.write(x)
f.close

# 仅仅是初步探索，syn shell以及具体逻辑待补全
