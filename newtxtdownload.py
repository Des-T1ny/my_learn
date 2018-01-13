import re
import requests
import json
import time

# 下载链接为   ：       http://www.wksw.la/




def getinfo(html):
	response = requests.get(html)
	response.encoding = 'gbk'
	maininfo = re.search('正文(.*?)<a name', response.text, re.S)
	info = re.findall('<a href="(.*?)">(.*?)</a>', maininfo.group(1), re.S)
	return info


def gettext(url, f):
	response = requests.get(url)
	response.encoding = 'gbk'
	maintext = str(re.findall('<div class="ccontent" id="ccontent">(.*?)</div>', response.text, re.S))
	text1 = re.findall('<br />&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />', maintext, re.S)
	text2 = re.findall("'(.*?);psbn&;psbn&;psbn&;psbn&>/ rb", str(maintext[::-1]), re.S)
	text2 = str(text2)[-3:1:-1]
	for each in text1:
		f.write(each+'\n')
	f.write(text2 + '\n\n\n\n\n\n\n\n')




if __name__ == '__main__':
	html = input("网页链接为：")
	name = input("书籍名称为：")
	# html = 'http://www.wksw.la/files/article/html/1/1356/'
	f = open(name+'.txt', 'w', encoding='utf-8')
	info = getinfo(html)
	for each in info:
		f.write(each[1]+'\n')
		print(each[1])
		try:
			gettext(html + each[0], f)
		except TimeoutError:
			time.sleep(10)
			gettext(html + each[0], f)
	f.close()




