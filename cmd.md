chmod -R 777 html

sudo ps -e |grep ssh

scp app-release.apk root@115.28.66.229:/root

netstat -an | grep 3306 #查看端口

netstat -tunlp|grep 端口号

tail -f LivePlaybackSplit.log 

find / -name 'nginx'

kill -HUP pid  //gunicorn  热部署

PS:

	HUP (1)是让进程挂起，睡眠;

	kill (9)六亲不认的杀掉

	term (15)正常的退出进程

pstree -ap |grep gunicorn   #查看gunicorn的进程列表


ffmpeg -i success.mp4 -metadata:s:v rotate="90" -codec copy output_success.mp4

ffmpeg -i test.mp4 -ss 10 -t 15 -codec copy cut.mp4

ffmpeg -i example.avi -vf crop=a:b:c:d  outputfilename

/etc/nginx/sites-enabled 


vim /etc/profile
export ANDROID_NDK=/root/android/android-ndk-r11c
export PATH=${PATH}:$NDK
source /etc/profile

DsMPyQPTK4Kj


ls -l |grep "^-"|wc -l

nginx rewrite模块：pcre库
nginx gzip模块：zlib库
nginx ssl模块：openssl库
rpm -q pcre
rpm -q zlib
rpm -q openssl
开启ssl 模块需要./configure执行时带上选项 --with-http_ssl_module
./configure --with-http_ssl_module
make
make install 


######################################################
centos 7
防火墙
启动防火墙 systemctl start firewalld.service

开启 80  端口
firewall-cmd --zone=public --add-port=80/tcp --permanent  

开启443 端口
firewall-cmd --zone=public --add-port=443/tcp --permanent 

重启防火墙
firewall-cmd --reload

查看防火墙端口状态
firewall-cmd --zone=public --list-ports

删除
firewall-cmd --zone=public --remove-port=20/tcp --permanent --永久删除卡对外开放的端口

查看
firewall-cmd --zone=public --query-port=80/tcp

######################################################

软链接
ln -s /usr/local/python3/bin/gunicorn /usr/bin/gunicorn


ffmpeg  -y -i 原视频.mp4 -vcodec copy -acodec copy -ss 00:00:04 -to 00:00:08 cut_time.mp4 