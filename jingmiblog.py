#coding = 'utf-8'

import re
import requests
import json
from bs4 import BeautifulSoup
import pdfkit



# url = input("url:")
url = 'https://cuiqingcai.com/1052.html'
response = requests.get(url).text
info = str(re.search('<p>以下为Python2爬虫系列教程(.*?)希望对大家有所帮助，谢谢！</p>',response,re.S).group(1))
titleandhref = re.findall('href="(.*?)"',info,re.S)
page = 1
for each in titleandhref:
	# href = each[1]
	# title = each[0]
	responseurl = requests.get(each)
	soup = BeautifulSoup(responseurl.content, 'html.parser')
	title = soup.find('title').get_text()
	body = soup.find_all(class_="article-content")[0]
	center_tag = soup.new_tag("center")
	title_tag = soup.new_tag('title')
	center_tag.insert(1,title_tag)
	body.insert(1, center_tag)
	html = str(body)
	print(html)
	html = html.encode('utf-8')

	with open(r'E:\W\test_spider\jingmiblog\\' + str(page) + '.html', 'wb') as f:
		f.write(html)
		page += 1


options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

#
# for i in range(page):
# 	pdfkit.from_file(str(i+1)+'.html', 'fukua.pdf', options = options)

