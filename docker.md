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