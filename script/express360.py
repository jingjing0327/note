import urllib.request
import time
import hashlib

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
	nu="SF1163107009254"
	# nu="YT2066479734282"
	strTime,token = getAjaxToken(nu,'1ec37a7b64060211662aae3f8b1de9d5');
	xx="https://open.onebox.so.com/api/getkuaidismart?com=&nu="+nu+"&time="+str(strTime)+"&token="+token
	print(xx)


