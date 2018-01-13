import requests
import json
import re
#

headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Mobile Safari/537.36'}

f = open('sina.txt', 'w', encoding = 'utf-8')
try:
	for i in range(20):
		url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3053244325&featurecode=10000326&type=uid&value=3053244325&since_id=' + str(i+1)
		response = requests.get(url, headers = headers)
		for i in range(20):
			try:
				info = response.json()['data']['cards'][0]['card_group'][i]['user']
				gender = str(info['gender'])
				# f.write(str(info)+'\n')
				if gender == 'f':
					name = str(info['screen_name'])
					descripition = str(info['description'])
					sinaurl = str(info['profile_url'])
					f.write('昵称：'+name)
					print(name)
					if descripition == '':
						pass
					else:
						f.write('    签名：'+descripition)
					f.write('      微博地址：'+sinaurl+'\n')
			except Exception as t:
				print('出现错误:' + t.__doc__)
except Exception as e:
	print (e.__doc__)
f.close()


