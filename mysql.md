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

