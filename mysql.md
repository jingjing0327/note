zip 安装版本

my.ini
	[mysqld]
	port=3306
	basedir=E:\\Program Files (x86)\\mysql-8.0.11-winx64\\mysql-8.0.11-winx64
	datadir=E:\\Program Files (x86)\\mysql-8.0.11-winx64\\mysql-8.0.11-winx64\\data
	max_connections=200
	max_connect_errors=10
	character-set-server=utf8
	default-storage-engine=INNODB
	default_authentication_plugin=mysql_native_password
	[mysql]
	default-character-set=utf8
	[client]
	port=3306
	default-character-set=utf8


打印出来原始密码：mysqld --initialize --console

mysqld --install

net start mysql

修改密码：mysqladmin -u root -p password

登录： mysql -u root -p


   [root@localhost src]# wget http://repo.mysql.com/mysql57-community-release-el7-8.noarch.rpm 

   [root@localhost src]# rpm -ivh mysql57-community-release-el7-8.noarch.rpm 

   [root@localhost src]#  yum -y install mysql-server 
根据步骤安装就可以了，


SET PASSWORD = PASSWORD('xhY69Mo%AGamjCxx');

ALTER USER 'root'@'localhost' PASSWORD EXPIRE NEVER;

flush privileges;


默认配置文件路径： 
配置文件：/etc/my.cnf 
日志文件：/var/log/var/log/mysqld.log 
服务启动脚本：/usr/lib/systemd/system/mysqld.service 
socket文件：/var/run/mysqld/mysqld.pid


GRANT USAGE ON *.* TO 'remote_lq'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
remote_lq   %   123456
User       Host  Password

CREATE DATABASE IF NOT EXISTS zi_wei DEFAULT CHARSET utf8 COLLATE utf8_general_ci;



授权
grant all privileges on zi_wei.* to 'remote_lq'@'%' identified by '123456';

grant all privileges on *.* to 'remote_lq'@'%' identified by '1';

123456 是密码！

flush privileges;

mysql 卡死
show processlist;

select trx_state, trx_started, trx_mysql_thread_id, trx_query from information_schema.innodb_trx\G

kill trx_mysql_thread_id


ALTER TABLE yuflx_zi DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;