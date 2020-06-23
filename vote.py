
import urllib2
import urllib
import random
import time

def get_data(url,xid):
	# get all data
	a=["3908","3915","3916","3917","3918","3919","3920","3921","3922","3923","3924","3925","3926"]
	b=["3909","3910","3927","3928","3929","3930","3931","3932","3933","3934","3935","3936","3937","3938","3939","3940","3941","3942","3943","3944","3945","3946","3947","3948"]
	c=["3955"]
	d=["3913","3914","3959","3960","3961","3962","3963","3964","3965"]
	formdata = {'vote' : '{"id":"455","options":[{"item_id":"580","option_id":"'+random.choice(a)+'"},{"item_id":"581","option_id":"'+random.choice(b)+'"},{"item_id":"582","option_id":"3955"},{"item_id":"583","option_id":"'+random.choice(d)+'"}]}',
		'clientInfo' : '{"platform":"web","account_id":-1,"session_id":"'+xid+'"}'
		}
	postdata = urllib.urlencode(formdata)
	req = urllib2.Request(url,postdata)
	request=urllib2.urlopen(req)
	data=request.read().decode('utf-8','ignore')
	return data

if __name__ == '__main__':
	a=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
	t=[0.5,0.6,0.7,0.8,0.9,1,1.2,1.3,1.4,1.5]
	for xx in range(1,100):
		xid=""
		for x in range(1,16):
			xid+=random.choice(a)
		time.sleep(random.choice(t))
		print(get_data("https://tool.8531.cn/index.php/Activity/component/component/action/save/appid/80_kU38r2AZPuVgVuNO/activity_id/455/key/"+xid,xid))

