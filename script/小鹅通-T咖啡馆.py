import json
import time
teacher=["中德讲师宋鹏程","大石","中德晓丽","中德讲师-徐星","中德讲师李夏文","钟建春","中德讲师赵小丹","中德讲师张环静","中德智慧讲师马迪","中德讲师-张磊","中德讲师李娜","中德智慧讲师陈树炎","中德智慧教育讲师—李春华","中德讲师王兰","中德讲师麻兰","中德讲师吴守家","中德智慧讲师齐宾","中德智慧讲师温秀丽","中德智慧讲师－杨田田","王海英"]
teacher_ids=["201","202","203","204","205","206","207","208","209","210","301","302","303","304","305","306","307","308","309","310"]
x_id=1137
sql_f=open("sql.txt","w",encoding="utf-8")
for xx in range(1,28):
	f=open("json-data/"+str(xx))
	j=json.loads(f.read())
	feedsInfo=j["data"]["feedsInfo"]
	for x in feedsInfo:
		nick_name=x["nick_name"]
		if nick_name in teacher :
			teacher_id=""
			for index,teacher_name in enumerate(teacher):
				if(teacher_name==nick_name):
					teacher_id=teacher_ids[index]
					break;

			talk_id=x_id*xx
			text=x["content"]["text"]
			title=text[:15]
			# x_id=x_id+1
			# sql_title='INSERT INTO luojigou_parent_talk_item(`id`,`talk_id`,`content`,`type`,`sort`,`width`,`height`) VALUES("'+str(x_id)+'","'+str(talk_id)+'","'+title+'",0,0,0,0);\n'
			x_id=x_id+1
			sql_content='INSERT INTO luojigou_parent_talk_item(`id`,`talk_id`,`content`,`type`,`sort`,`width`,`height`) VALUES("'+str(x_id)+'","'+str(talk_id)+'","'+text+'",1,1,0,0);\n'

			if "img" in x["content"]:
				imgs= x["content"]["img"]
				for index,img in enumerate(x["content"]["img"]):
					width=x["content"]["img_info"][index]["0"]
					height=x["content"]["img_info"][index]["1"]
					sort=index+2
					x_id=x_id+1
					sql_img='INSERT INTO luojigou_parent_talk_item(`id`,`talk_id`,`content`,`type`,`sort`,`width`,`height`) VALUES("'+str(x_id)+'","'+str(talk_id)+'","'+img+'",2,'+str(sort)+','+str(width)+','+str(height)+');\n'
					print(sql_img)
					sql_f.write(sql_img)
				
				x_sql=r'INSERT INTO luojigou_parent_talk(`id`,`title`,`img_cover`,`user_id`,`category_id`,`width`,`height`,`user_type`) VALUES("'+str(talk_id)+'","'+title+'...","'+imgs[0]+'","'+teacher_id+'","1","'+width+'","'+height+'","1");\n'
				sql_f.write(x_sql)
				# print(sql_title)
				# sql_f.write(sql_title)
				# print(sql_content)
				sql_f.write(sql_content)
