# install
yum update
yum install docker
systemctl start docker

### docker仓库 https://hub.docker.com

# docker in install mysql
	docker pull mysql
	cmd docker pull mysql:tag

# search: docker search mysql
	OFFICIAL 是否是官方

# 查看所有本地镜像
	docker images

# 删除指定的本地镜像
	docker rm image-id

# 运行
	docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

# 列表
	docker ps 查看运行中的容器 （加上-a 可以查看所有容器)
# 启动
	docker start container-name/container-id
# 停止
	docker stop container-name/container-id
# 删除
	docker rm container-id
# 端口映射
	-p 3307:3306 ----3307是本机的端口，3306是docker的端口
# 容器日志
	docker logs container-name/container-id
# mysql run
	docker run --name luojigou_001 -e TZ=Asia/Shanghai -p 3307:3306 -e MYSQL_ROOT_PASSWORD=asdfg12345 -d mysql:tag 
# mysql 进入系统命令
	docker exec -it luojigou_001 bash
	mysql -uroot -p
	输入密码，正常是用
	show databases;
	show tables;
	
# MySQL8.0的caching_sha2_password问题
然后输入ALTER USER root IDENTIFIED WITH mysql_native_password BY 'asdfg12345.';，然后调用下命令FLUSH PRIVILEGES;


### nginx
# 启动
$ docker run --name runoob-nginx-test -p 8081:80 -d nginx


### 首先，创建目录 nginx, 用于存放后面的相关东西。
mkdir -p ~/nginx/www ~/nginx/logs ~/nginx/conf
#拷贝容器内 Nginx 默认配置文件到本地当前目录下的 conf 目录，容器 ID 可以查看 docker ps 命令输入中的第一列：
docker cp 6dd4380ba708:/etc/nginx/nginx.conf ~/nginx/conf
www: 目录将映射为 nginx 容器配置的虚拟目录。
logs: 目录将映射为 nginx 容器的日志目录。
conf: 目录里的配置文件将映射为 nginx 容器的配置文件。
#部署命令
$ docker run -d -p 8082:80 --name runoob-nginx-test-web -v ~/nginx/www:/usr/share/nginx/html -v ~/nginx/conf/nginx.conf:/etc/nginx/nginx.conf -v ~/nginx/logs:/var/log/nginx nginx





###docker 时间不对
apt-get update
apt-get install vim 
vim /etc/mysql/my.conf
在[mysqld]下增加
default-time-zone = '+08:00'


### redis
docker run -p 6380:6379 --name luojigou_redis -v /usr/local/redis/conf/redis.conf:/etc/redis/redis.conf -v /usr/local/redis/data:/data -d redis redis-server /etc/redis/redis.conf --appendonly yes

https://redis.io/topics/config/ 这个地址可以下载redis的配置文件，我下载的是3.2版本的。

下载下来以后修改几个地方：

daemonize no#用守护线程的方式启动 （需要注意，如果是yes，redis是创建后会连不上，这个是个大坑，尤其要注意一下）

requirepass yourpassword#给redis设置密码

bind 127.0.0.1 #注释掉这部分，这是限制redis只能本地访问

appendonly yes#redis持久化


### php

docker run --name myphp -p 9001:9000 -v /root/php/www/:/var/www/html/ --privileged=true -d php:5.6-fpm
docker run --name myphp7 -p 9002:9000 -v /root/php/www/:/var/www/html/ --privileged=true -d php:7.1-fpm

/root/php/www/ 为主机的地址
/var/www/html/ 为虚拟机地址
--privileged=true 
	在Cent OS 7中运行,如果不加--privileged=true,则会出现nginx没有访问内部文件的权限
	原因是CentOS7中的安全模块selinux把权限禁掉了，至少有以下三种方式解决挂载的目录没有权限的问题：
	1，在运行容器的时候，给容器加特权：--privileged=true
	2，临时关闭selinux：
	su -c "setenforce 0"
	3，添加selinux规则，将要挂载的目录添加到白名单：
	chcon -Rt svirt_sandbox_file_t /var/www/html/xx/www/

宿主nginx的配置：
	server {
	    listen       8080;
	    server_name  *.lqcode.cn;
	    location ~ \.php$ {
	        root           /root/php/www;
	        fastcgi_pass   127.0.0.1:9001;
	        fastcgi_index  index.php;
	        fastcgi_param  SCRIPT_FILENAME /var/www/html/$fastcgi_script_name;
	        include        fastcgi_params;
	    }
	}
解释：root  /root/php/www;  为本机地址
fastcgi_pass   127.0.0.1:9001;  php 端口地址
fastcgi_param  SCRIPT_FILENAME /var/www/html/$fastcgi_script_name;   /var/www/html/ 为虚拟机的地址

php出现静态页面Access Denied.
find / -name "www.conf"
vim www.conf
找到下面这句，注释打开,注释是";",重启容器 docker restart myphp7
security.limit_extensions = .html .htm .php .js .css .jpg .jpeg .gif .png


php docker安装gd库扩展

apt update  #更新软件源
apt install -y libwebp-dev libjpeg-dev libpng-dev libfreetype6-dev #安装各种库
docker-php-source extract #解压源码
cd /usr/src/php/ext/gd  #gd源码文件夹
docker-php-ext-configure gd --with-webp-dir=/usr/include/webp --with-jpeg-dir=/usr/include --with-png-dir=/usr/include --with-freetype-dir=/usr/include/freetype2   #准备编译
docker-php-ext-install gd   #编译安装
php -m | grep gd
docker restart myphp7


php安装扩展：pdo_mysql
docker-php-ext-install pdo pdo_mysql
如果报 /usr/local/bin/docker-php-ext-enable: cannot create /usr/local/etc/php/conf.d/docker-php-ext-pdo_mysql.ini: Directory nonexistent
解决方案：
直接在/usr/local/etc/php目录下面新建 conf.d目录和对应的docker-php-ext-pdo_msql.ini文件
其中docker-php-ext-pdo_msql.ini的内容为：
extension=pdo_mysql.so

php安装扩展：zip
apt-get install -y --no-install-recommends libzip-dev 
docker-php-ext-install -j$(nproc) zip

php安装扩展：mysqli
cd /usr/local/bin
./docker-php-ext-install mysqli

# httpd
docker run --name httpd -d --restart always -p 81:80 -v /docker/httpd/html:/var/www/html -v /docker/httpd/logs:/etc/httpd/logs httpd

https://blog.csdn.net/bingzhongdehuoyan/article/details/79424340



docker 权限问题
docker exec -u root -it 9cd0966e1a81 bash