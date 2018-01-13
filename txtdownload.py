# encoding = 'utf-8'
# 小说下载网址为 https://www.ybdu.com/
import re
import requests
import time


def add_address(url):
	return (URL+url)
URL = input('网址链接为：')
# URL = 'https://www.ybdu.com/xiaoshuo/12/12814/'
txtname = input('小说名字为：')
f = open(txtname + '.txt', 'w', encoding = 'utf-8')  #打开文件
response = requests.get(URL)           #获取网页信息
response.encoding = 'gbk'              #resoponse转码
html = re.findall(' <ul class="mulu_list">(.*)</ul>', response.text, re.S)
html = str(html)
html = re.findall('href="(.*?)"', html, re.S)       #匹配章节网页

for each in html:
	txthtml = add_address(each)
	try:
		response1 = requests.get(txthtml)
	except Exception:
		response1 = requests.get(txthtml)
	response1.encoding = 'gbk'
	title = re.findall('<title>(.*?)_', response1.text, re.S)
	title = str(title)[2:-2]                          #获取章节名
	txtmain_re = re.findall('class="contentbox">(.*)<div', response1.text, re.S)
	txtmain_re = str(txtmain_re)                #获取正文
	txtmain = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /', txtmain_re, re.S)
	txtmain_re = txtmain_re[::-1]               #章节文本取反


	txtremain = re.findall(r'elyts_wohs>tpircs<>"00da"=ssalc vid<        n\\r\\(.*?);psbn&;psbn&;psbn&;psbn&>/', txtmain_re, re.S)
	txtremain = str(txtremain)[2:-2]            #获取章节最后一段
	txtremain = txtremain[::-1]                 #最后一段取反
	f.write(title + '\n')
	print(title)
	for abc in txtmain:
		f.write(abc+ '\n')
	f.write(txtremain+'\n\n\n\n\n')


f.close
