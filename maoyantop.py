# encoding = 'utf-8'

import re
import requests
import json
# import

def geturl(i):
	URL = 'http://maoyan.com/board/4?offset='
	url = URL + str(i*10)
	return url

# <dl class="board-wrapper">.*?t
if __name__ == "__main__":
	head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
	f = open('maoyantop.txt', 'w', encoding='utf-8')
	for i in range(10):
		url = geturl(i)
		html = requests.get(url, headers = head).text
		essay = re.findall('itle="(.*?)" clas.*?data-src="(.*?)" a.*?"star">\\n     (.*?)\\n.*?time">(.*?)</p>',html,re.S)
		print(essay[0])
		for each in essay:
			each = str(each)
			f.write(each + '\n')
	f.close()