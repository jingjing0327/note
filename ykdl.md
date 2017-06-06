## ykdl 修改文件
	youku.py
		61-65
		urls.append((u['cdn_url'],u['total_milliseconds_video']))
		# if u['key'] != -1:
		#     urls.append(json.loads(get_content(u['cdn_url']+'&yxon=1&special=true'))[0]['server'])
		# else:
		#     self.logger.warning("VIP video, ignore unavailable seg: {}".format(s['segs'].index(u)))

	acorig.py
		31-33
        stream_urls=[]
        for x in s['segs']:
            stream_urls.append((x['url'],x['total_milliseconds_video']))
        size = s['total_size']

    bilibili.py
		24-25
        length=durl.getElementsByTagName('length')[0].firstChild.nodeValue
        urls.append((durl.getElementsByTagName('url')[0].firstChild.nodeValue,length))