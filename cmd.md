chmod -R 777 html

sudo ps -e |grep ssh

scp app-release.apk root@115.28.66.229:/root

netstat -an | grep 3306 #查看端口

tail -f LivePlaybackSplit.log 

find / -name 'nginx'

kill -HUP pid  //gunicorn  热部署

PS:

	HUP (1)是让进程挂起，睡眠;

	kill (9)六亲不认的杀掉

	term (15)正常的退出进程

pstree -ap |grep gunicorn   #查看gunicorn的进程列表