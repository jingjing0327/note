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
        
    iqiyi.py
    	84-87
        duration=seg_info['d']
        str_duration=str(duration)+'000'
        down_url = json_data['l']
        real_urls.append((down_url,duration))
    acfun.py
        user_sourceVid=match1(self.url,r'id=([0-9]*)')
        if(user_sourceVid is None):

            html = get_content(self.url)

            sourceVid = match1(html, "data-vid=\"([a-zA-Z0-9=]+)\" data-(scode|cid)=")
        else:
            sourceVid=user_sourceVid

