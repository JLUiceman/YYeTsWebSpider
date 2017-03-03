#!/bin/python
#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import time
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
			print response.read().decode("gbk").encode("utf-8")
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
	num = 0
	soup = BeautifulSoup(data, 'html.parser')
	for mangent in soup.find_all('dd'):
		if mangent.find_all('a')[0].get_text().count('WEB-HR') > 0: #只抓取web-hr的资源
			f.write(mangent.find_all('a')[0].get_text()[22:28] + ':' +mangent['ed2k'] + '\n')
			num = num + 1
	else:		
		return num		

def getNum(data):
	soup = BeautifulSoup(data, 'html.parser')
	sourceStr = soup.find_all("div",class_="pages")[0].get_text()
	return sourceStr[sourceStr.index('/')+1]		


def init(obj):
	num = getNum(obj.getData(1))
	allNum = 0
	while num > 0 :
		d = yyets.getData(num)
		allNum = allNum + getContent(d)
		num = int(num) - 1
	else:
		f2 = open('/home/node-server/workspace/YYeTsWebSpider/synRes.log', 'a')
		f2.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '同步结果共' + str(allNum) + '条\n')
		f2.close()
		f.close	

f = open('/home/node-server/workspace/YYeTsWebSpider/yyRes.json', 'w+')	
yyets = YYeTs('行尸走肉')	

init(yyets)	

