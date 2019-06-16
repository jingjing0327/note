# install
yum update
yum install docker
systemctl docker

### docker仓库 https://hub.docker.com

# docker in install mysql
	docker pull mysql
	cmd docker pull mysql:tag

# search: docker search mysql
	OFFICIAL 是否是官方

# 查看所有本地镜像
	docker images

# 删除指定的本地镜像
	docker rmi image-id

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
	docker run --name luojigou_001 -p 3307:3306 -e MYSQL_ROOT_PASSWORD=asdfg12345 -d mysql:tag 
# mysql 进入系统命令
	docker exec -it luojigou_001 bash
	mysql -uroot -p
	输入密码，正常是用
	show databases;
	show tables;
	



