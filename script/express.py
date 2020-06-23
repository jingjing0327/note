import urllib.request

def get_data(url):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read().decode('utf-8','ignore')
	return data

if __name__ == '__main__':
	# url="https://m.baidu.com/s?word=%E5%BF%AB%E9%80%92%E6%9F%A5%E8%AF%A2"
	url="https://m.so.com/s?q=%E5%BF%AB%E9%80%92"
	print(get_data(url))