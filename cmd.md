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