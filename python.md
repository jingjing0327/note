## python
# open 文件正确打开方式
	```python
	import codecs
	--------
	aa=codecs.open("gif.txt",'a','utf-8')
	------------------------------------
	_file=open("city.json",'r',encoding= 'UTF-8')
	------------------------------------
	<!-- 乱码解决方法 -->
	# -*- coding: UTF-8 -*-
	#!/usr/bin/python
	f = open("qudao.txt", "rb")
	strxx='' 
	for line in f:
		line= str(line, encoding = "utf-8")
		strxx+='"'+line.strip('\r\n')+'",'
	print(strxx) 
	f.close()  

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


	def get_data(url):
		# get all data
		headers ={'User-Agent':"xxx"}
		req=urllib.request.Request(url)
		req.add_header('Referer', 'http://wwww.lqcode.com')
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
		f=urllib.request.urlopen(req)
		datax=f.read().decode('utf-8','ignore')

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
	class 直接转成json 报 TypeError: Object of type 'Result' is not JSON serializable
	需要用lambda表达式转移一下
	return json.dumps(result,default=lambda obj:obj.__dict__,sort_keys=True,indent=4)
		lambda obj: obj.__dict__          会将任意的对象，转换成字典的方式

		sort_keys=True                    会按照字典中的键来按照ASCII方式来排序

		indent=4                          会按照键值对以间隔4来直观的显示

	json.dumps(out_json_str, default=lambda o: o.__dict__, sort_keys=True, indent=4)
	```
# install
	zipimport.ZipImportError: can't decompress data; zlib not available
	解决方法：
		1、安装依赖zlib、zlib-devel
		2、重新编译安装Python
	
	./configure 
	编辑Modules/Setup文件 
	找到下面这句，去掉注释 
	#zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz 
	重新编译安装：make & make install 

ps -fA | grep python
nohup python3 -u app.py > app.log &

# python 头
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

# flask 启动端口
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	from flask import *


	app = Flask(__name__)

	@app.route("/")
	def root():
	    return "czxy_xxx"

	if __name__ == '__main__':
	    app.run(host='0.0.0.0')
	    
# mysql
	```python
	def conn():
	my_connect=pymysql.connect(host='127.0.0.1',
							 user='root',
							 password='asdfg12345',
							 db='test',
							 charset='utf8',
							 cursorclass=pymysql.cursors.DictCursor)
	my_cursor=my_connect.cursor();
	my_cursor.execute("select * from `abc`")
	my_result=my_cursor.fetchall();
	my_cursor.close()
	my_connect.close()
	return my_result	    
	```
# 正则表达式
------------------------
<.*View\n\s*android:id=\"@\+id/[a-z0-9_]*\"	
------------------------
<TextView
            android:id="@+id/new_update_tip"
------------------------

# flash post 获取参数
		_data=request.get_json();  //get_json()获取前台传过来的json
		company=Company(**_data)	//json 转成对象
		
		// 前台 ajax的正常访问姿势,以json的形式来访问
		$.ajax({
			              type:"POST",
			              url:SERVER_IP+"add_company",
			              data:JSON.stringify({"company_name":this.company_name,
			              "company_client_name":this.company_client_name,
			              "company_phone":this.company_phone,
			              "cz_name":this.cz_name,
			              "state":this.state,
			              "company_info":this.company_info}),
			              dataType:"json",
			              contentType: 'application/json;charset=utf-8',
			              success:function(data){
			              	console.log("success")
			              },
			              error:function () {
			                console.log("error")
			              }
			        	});
			        	
# 时间
		create_time=item['create_time']
		d = datetime.datetime.fromtimestamp(create_time)  
		create_time = d.strftime("%Y-%m-%d %H:%M:%S")

# gunicorn 使用守护进程
		gunicorn -w 4 -b 0.0.0.0:616 dr_app:app &

		nohup python -u test.py > nohup.out 2>&1 &    //-u 无缓冲，直接打印到日志

# 透明图片粘贴
	import Image

	background = Image.open("test1.png")
	foreground = Image.open("test2.png")

	background.paste(foreground, (0, 0), foreground)
	background.show()

# python 裁剪成圆形
	head = Image.open('head.jpg')
	bigsize = (head.size[0] * 3, head.size[1] * 3)
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + bigsize, fill=255)
	mask = mask.resize(head.size, Image.ANTIALIAS)
	head.putalpha(mask)
	head_w_p=(int(x_width/2)-int(head_w/2))
	head_h_p=int(last_h-head_h/2)
	toImage.paste(head,(head_w_p,head_h_p),head)
# python gunicorn

	gunicorn app:app -c gunicorn.conf
	gunicorn app668:app -c gunicorn.conf
	conf如下：
		workers = 4
		bind = '0.0.0.0:616'
		daemon = True
		timeout = 120
		accesslog = 'acess.log'
		errorlog = 'error.log'
			