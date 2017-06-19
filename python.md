## python
# open 文件正确打开方式
	```python
	import codecs
	aa=codecs.open("gif.txt",'a','utf-8')
	```
# 递归超过最大范围
	```python
	import sys
	sys.setrecursionlimit(8000)
	```
# 网络访问
	```python
	python3

	import urllib.request
	def get_data(url):
		# get all data
		req=urllib.request.Request(url)
		f=urllib.request.urlopen(req)
		data=f.read().decode('utf-8','ignore')
		return data

	-------------------------------------
	python2

	def get_data(url):
	    # get all data
	    request=urllib.urlopen(url)
	    data=request.read().decode('utf-8','ignore')
	    return data
	```
# 正则表达式
	```python
	import re
	pattern_item_gif=re.compile(r'<a href="(http://www.gifjia.com/[0-9]{1,8}/[0-9]{1,5}/)"><span>[0-9]{1,3}</span></a>')
	search_item_gif=pattern_item_gif.findall(str(data))
	return search_item_gif
	```
# 创建class
	```python
	class item(object):
    def __init__(self,pic,shortTitle,url,vt):
        self.pic = pic
        self.shortTitle=shortTitle
        self.url=url
        self.vt=vt
    -----------------------------
	use:
    	item(pic,shortTitle,url,vt)
	```
# python2 utf-8

	```python

	import sys
	reload(sys)   
	sys.setdefaultencoding('utf8') 
	```
# JSON
	```python
	json.dumps(out_json_str, default=lambda o: o.__dict__, sort_keys=True, indent=4)
	```
