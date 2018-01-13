#encoding = 'utf-8'


import requests
from bs4 import BeautifulSoup
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}




def get_main():
	print('小说网址主页：https://www.ybdu.com/' + '\n')
	global catalog_url
	catalog_url = input('请输入小说目录网址：')
	# catalog_url = 'https://www.ybdu.com/xiaoshuo/12/12814/'


def get_info(url):
	try:
		info = requests.get(url)
	except Exception as e:
		print(e.__doc__)
		info = get_info(url)
	return info

def link_url(url1, url2):
	return url1+url2

def get_txt_name(info):
	soup = BeautifulSoup(info.content, 'html.parser')
	txtname = re.findall("'(.*?)'", str(soup.find('script').string), re.S)
	with open(txtname[0] + '.txt', 'w', encoding = 'utf-8') as f:
		pass
	return txtname[0]

def chapter_urlANDname(info):
	soup = BeautifulSoup(info.content, 'html.parser')
	urls = soup.find_all('a', href = re.compile('^\d*?.html'))

	chapter_url = []
	chapter_name = []
	for each in urls:
		# print(each['href']+' '+each.string)
		chapter_url.append(link_url(catalog_url, each['href']))
		chapter_name.append(each.string)
	# print(chapter_url)
	# print(chapter_name)
	return [chapter_name, chapter_url]

def get_essayANDwrite_to_txt(charpter_name,url):
	info = get_info(url)
	soup = BeautifulSoup(info.content, 'html.parser')
	html = soup.find('div', id = 'htmlContent', class_ = 'contentbox')
	print(charpter_name + '       ' + url)
	f = open(txtname + '.txt', 'a+', encoding = 'utf-8')
	essay = []
	f.write(charpter_name)
	for i in html.children:
		if i.string == None:
			pass
		elif i.string == 'show_style();':
			break
		else:
			f.write(i.string + '\n')
			#print(i.string)
			# essay.append(str(i.string))
	f.close()












if __name__ == '__main__':
	# get_name()
	get_main()
	info = get_info(catalog_url)
	global txtname
	txtname = get_txt_name(info)
	urlANDname = chapter_urlANDname(info)
	for page in range(len(urlANDname[0])):
		get_essayANDwrite_to_txt(urlANDname[0][page], urlANDname[1][page])






