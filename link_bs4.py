#encoding = 'utf-8'

import requests
from bs4 import BeautifulSoup
import re
#引用

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}


url = 'http://www.baidu.com'
info = requests.get(url, headers = headers)
soup = BeautifulSoup(info.content, 'html.parser')

# print(soup)
print(soup.prettify())    #按html格式输出网页源代码

print(soup.a)
print(soup.a.attrs)
print(soup.a['href'])
children = soup.a.children                  #获得第一个a标签的所有子节点，需遍历才能得到每一个子节点的信息
for child in children:                     #遍历以得到子节点的信息
	print(child)
print(soup.a.contents)                      #获得第一个标签的所有子节点，返回一个列表
print(soup.a.contents[0])                   #获得第一个a标签的第一个子节点的内容
print(soup.a.contents[0]['alt'])           #获得第一个a标签的第一个子节点中的alt信息
print(soup.a.contents[0]['src'])           #获得第一个a标签的第一个子节点中的src的信息
print(soup.a.contents[0]['title'])         #获得第一个标签的第一个子节点中的title的信息
# html = soup.find_all('a', href = re.compile('(http:.*?)'))            #得到所有满足正则表达式的a标签
# for a in html:
# 	print(a['href'])
# for b in soup.strings:                   #打印网页所有标签的内容
# 	print(b)
for c in soup.find_all('a'):              #获得所有a标签的内容
	print(c.string)
print(soup.b)                             #打印第一个b标签







