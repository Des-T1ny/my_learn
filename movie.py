# encoding = 'utf-8'

import re
import requests
import json
import time
from multiprocessing import Pool
def addadress(url, page):
	page = str(page)
	return url + '/page/' + page

def getnameandurl(eachclassurl):
	page = 1
	nameandurl = {}
	f = open('moviex.txt', 'a', encoding='utf-8')
	while True:
		eachpage = addadress(eachclassurl, page)
		response = requests.get(eachpage).text
		meach = re.findall("<!-- blog列表-->(.*?)<!--blog列表结束 -->", response, re.S)
		while meach == []:
			f.close()
			return
		meach = str(meach)
		meach = re.findall(('<h2><a href="(.*?)" title='), meach, re.S)
		for each in meach:
			title = gettitle(each)
			# print((title))
			nameandurl = {title:each}
			f.write(json.dumps(nameandurl, ensure_ascii=False) + '\n')

		page += 1



def gettitle(url):
	response = requests.get(url).text
	title = re.search('<title>(.*?)_天天看美剧</title>', response, re.S).group(1)
	# print(type(title))
	return title


def geturl():
	url = 'http://www.msj1.com/'
	response = requests.get(url).text
	mclass = re.search('首页</a></li>(.*?)menu-item-5428"', response, re.S)
	classurl = re.findall('href="(.*?)">', mclass.group(1), re.S)
	return classurl

def main(processings):
	classurl = geturl()
	print(len(classurl))
	getnameandurl(classurl[processings])
	# for eachclassurl in classurl:
	# 	print('正在抓取第%d类，请等待'%i)
	# 	nameeandurl = getnameandurl(eachclassurl, nameandurl)
	# nameandurl = getnameandurl(classurl[processings], nameandurl)
	# f = open('movie.txt', 'a', encoding='utf-8')
	# f.write(json.dumps(nameandurl, ensure_ascii=False) + '\n')
	# f.close()


if __name__ == "__main__":
	# pool = Pool()
	# pool.map(main,range(9))
	# main(1)
	for i in range(9):
		main(i)


