
import urllib2
import urllib
import random

def get_data(url):
	# get all data
	a=["3834","3835","3836","3837","3838","3839","3840","3841","3842","3843","3844","3845","3846","3847"]
	b=["3848","3849","3850","3851","3852","3853","3854","3855","3856","3857","3858","3859","3860","3861","3862","3863","3864","3865","3866","3867","3868","3869","3870","3871"]
	c=["3880"]
	d=["3884","3885","3886","3887","3888","3889","3890","3891","3892","3893"]
	formdata = {'vote' : '{"id":"450","options":[{"item_id":"572","option_id":"'+random.choice(a)+'"},{"item_id":"573","option_id":"'+random.choice(b)+'"},{"item_id":"574","option_id":"3880"},{"item_id":"575","option_id":"'+random.choice(d)+'"}]}',
		'clientInfo' : '{"platform":"web","account_id":-1,"session_id":"f53dcbedfa6a2a6d"}'
		}
	postdata = urllib.urlencode(formdata)
	req = urllib2.Request(url,postdata)
	request=urllib2.urlopen(req)
	data=request.read().decode('utf-8','ignore')
	return data

if __name__ == '__main__':
	a=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
	for xx in range(1,100):
		xid=""
		for x in range(1,16):
			xid+=random.choice(a)
		print(get_data("https://tool.8531.cn/index.php/Activity/component/component/action/save/appid/80_kU38r2AZPuVgVuNO/activity_id/450/key/"+xid))