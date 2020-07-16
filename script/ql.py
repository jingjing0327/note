import urllib.request
import json
import os

def get_data(url):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read().decode('utf-8','ignore')
	return data

def save_data(url,name):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read()
	file=open(name,"wb")
	file.write(data)
	file.close()


# if __name__ == '__main__':
# 	content=open("ql.json",'r',encoding='UTF-8').read()
# 	j=json.loads(content)
# 	index=84;
# 	for x in j["data"]["liveSpeakViews"]:
# 		if(x["type"]=="audio"):
# 			index=index+1;
# 			save_data(x["content"]+".m4a",str(index)+".m4a")
# 		if(x["type"]=="image"):
# 			index=index+1;
# 			save_data(x["content"],str(index)+".png")

if __name__ == '__main__':
	f=os.listdir(r"C:\Users\Administrator\Desktop\441B.W._files")
	for index,x in enumerate(f):
		url="https://p0.meituan.net/wmproduct/"+x
		url=url.replace("@75w_75h_80Q_0e_1l.webp","")
		print(url)
		save_data(url,str(index)+".jpg")
	# f.sort(key= lambda x:int(x[:-4]))
	# for x in f:
	# 	if("m4a" in x):	
	# 		print("file '"+x+"'")
