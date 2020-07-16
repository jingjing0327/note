import urllib.request
import time
import hashlib
import sys

def get_data(url):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read().decode('utf-8','ignore')
	return data

def getAjaxToken(nu,key):
	strTime=int(time.time())
	params="com"+""+"nu"+nu+"time"+str(strTime)+key
	token=hashlib.md5(params.encode(encoding='UTF-8')).hexdigest()
	return strTime,token


if __name__ == '__main__':
	key=sys.argv[0]
	nu=sys.argv[1]
	# nu="SF1163107009254"
	# nu="YT2066479734282"
	strTime,token = getAjaxToken(nu,key);
	xx="https://open.onebox.so.com/api/getkuaidismart?com=&nu="+nu+"&time="+str(strTime)+"&token="+token
	print(xx)



