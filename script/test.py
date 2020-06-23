
import urllib.request
def get_data(url):
	# get all data
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read().decode('utf-8','ignore')
	return data

if __name__ == '__main__':
	x=get_data("http://store.suizhi.com/DRM/mobile/store/discovery?username=ph1591923316449&token=fd62bb3c4a8e4d98105f52539a9b0dc4&currentPageNum=1&application_name=SuiZhi_for_Android&app_version=3.2.3&IMEI=null")
	print(x)