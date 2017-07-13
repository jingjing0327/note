## sql

order by NO desc
这里的NO值为：7，8，9，10，数据类型为 varchar
出现排序的时候，变成了 9,8,7,10
解决方法：
	order by CAST(NO as SIGNED) desc
转成int

mysql为我们提供了两个类型转换函数：CAST和CONVERT，现成的东西我们怎能放过？

CAST() 和CONVERT() 函数可用来获取一个类型的值，并产生另一个类型的值。
这个类型 可以是以下值其中的 一个：
BINARY[(N)]
CHAR[(N)]
DATE
DATETIME
DECIMAL
SIGNED [INTEGER]
TIME
UNSIGNED [INTEGER]

 

所以我们也可以用CAST解决问题：

select server_id from cardserver where game_id = 1 order by CAST(server_id as SIGNED) desc limit 10



也可以使用CONVERT来搞定此问题：

select server_id from cardserver where game_id = 1 order by CONVERT(server_id,SIGNED) desc limit 10