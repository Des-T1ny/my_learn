# encoding = 'utf-8'


import re
import requests
from bs4 import BeautifulSoup
import time
headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            'Referer': "http://www.mzitu.com/"
        }



def link_url(url1,url2):
	return url1+url2



def get_info(url):
	try:
		# time.sleep(5)
		info = requests.get(url,headers = headers)
	except Exception as e:
		print(e.__doc__)
		info = get_info(url)
	return info



def get_gather(info):
	soup = BeautifulSoup(info.content, 'html.parser')
	url = soup.find_all('li')
	flag = 0
	png_name = []
	png_url = []
	for each in url:
		if flag > 6:
			png_name.append(each.contents[1].string)
			png_url.append(each.contents[0]['href'])
		flag += 1
	return [png_name,png_url]


def get_jpg(info, name):
	soup = BeautifulSoup(info.content, 'html.parser')
	jpg = soup.find('img', alt=name)['src']
	write_jpg(jpg,name,0)
	print(jpg)
	max_page = int(soup.find('div', class_ = "pagenavi").contents[-3].contents[0].string)
	for page in range(1,max_page+1):
		if page < max_page :
			next_page = soup.find('div', class_='pagenavi').contents[-2]['href']
			info = get_info(next_page)
			soup = BeautifulSoup(info.content, 'html.parser')
			jpg = soup.find('img', alt=name)['src']
			print(jpg)
			write_jpg(jpg,name,page)






def write_jpg(data,name,page):
	try:
		jpg = requests.get(data, headers=headers).content
	except Exception as e:
		print(e.__doc__)
	with open(name + str(page) + '.jpg','wb') as f:
		f.write(jpg)



if __name__ == '__main__':
	for page in range(163):
		url = link_url('http://www.mzitu.com/page/', str(page+1))
		info = get_info(url)
		name_and_url = get_gather(info)
		for number in range(len(name_and_url[0])):
			info = get_info(name_and_url[1][number])
			get_jpg(info, name_and_url[0][number])
			break






