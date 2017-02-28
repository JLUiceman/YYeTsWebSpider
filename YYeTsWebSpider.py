#!/bin/python
#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import os

baseUrl = 'http://cili17.com/?topic_title3='

class YYeTs:
	def __init__(self, keyWord):
		#python3.x版本需要使用urllib.pare.quote
		self.url = baseUrl + urllib.quote(keyWord)

	def getData(self, pageNum):
		url = self.url + '&p=' + str(pageNum)

		try:
			req = urllib2.Request(self.url)
			response = urllib2.urlopen(req)
			return response.read()
		except urllib2.HTTPError, e:
			print BeautifulSoup(e.read(), "html.parser")
			print e.code
		except urllib2.URLError, e:
			print e.reason
		else:
			print 'get it'
		finally:
			pass

def getContent(data):
	soup = BeautifulSoup(data, 'html.parser')
	for mangent in soup.find_all('dd'):
		if mangent.find_all('a')[0].get_text().count('WEB-HR') > 0: #只抓取web-hr的资源
			f.write(mangent.find_all('a')[0].get_text()[22:28] + ':  ' +mangent['ed2k'] + '\n')

def getNum(data):
	soup = BeautifulSoup(data, 'html.parser')
	sourceStr = soup.find_all("div",class_="pages")[0].get_text()
	return sourceStr[sourceStr.index('/')+1]		


def init(num):
	while num > 0 :
		d = yyets.getData(num)
		getContent(d)
		num = int(num) - 1
	else:
		f.close	

f = open('yyRes.json', 'w+')	
yyets = YYeTs('行尸走肉')	
num = getNum(yyets.getData(1))

init(num)	

