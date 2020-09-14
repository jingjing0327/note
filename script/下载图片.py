import urllib.request
import json
import os

def get_data(url):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read().decode('utf-8','ignore')
	return data

def save_data(url,name):
	req=urllib.request.Request(url)
	f=urllib.request.urlopen(req)
	data=f.read()
	file=open(name,"wb")
	file.write(data)
	file.close()


# if __name__ == '__main__':
# 	content=open("ql.json",'r',encoding='UTF-8').read()
# 	j=json.loads(content)
# 	index=84;
# 	for x in j["data"]["liveSpeakViews"]:
# 		if(x["type"]=="audio"):
# 			index=index+1;
# 			save_data(x["content"]+".m4a",str(index)+".m4a")
# 		if(x["type"]=="image"):
# 			index=index+1;
# 			save_data(x["content"],str(index)+".png")

if __name__ == '__main__':
	pics=["http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1td0NUWXRESw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1YVmRFdXByVw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi1mZzN6TWxMWQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS0xSnhzYWhmMw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC14U1N2NnZmRQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1ncGF3RExadg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1qWjhQc1ZuOA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS1SYjZXNUhvcg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS0xNnR2cUJDTQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS12SlhtdllPTg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1ua0dWZWx6TA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS1wZ1E5UVd3eA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1naTZTS1V5VA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS00eU5ZbEJmeg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1LdVBBeUpoNw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1BdUdpc1RZdw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC1nN3FvR24xNw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC1jOHFReWF2dw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS12ODhXblBjMQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS1qbVNnbjJ6Tg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS14NWNueEJVQg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi1mMFh1akxUQw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS1vTm5XZ1pnMw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1PZTZGSnpzSA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS11WDRLRzVuNA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi1aTFlhR2dpRg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi1zM1Bzd0M2NQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi1iZE9UaDFScw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA3ZGI0MDY3YWJfVzk5dGI3TG1HaC1RcndZMjN0WQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA3ZGI0MDY3YWJfVzk5dGI3TG1HaC1SQU42OGluMQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS02eWRSQnRGcQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS01a1RJNzBWRw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1wZW00c0FTeQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS1DblNVSHVMVQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS03VVRQTEFnNQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS1ieWVZOUZqYw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS14ODFqbnlkcA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1WbnUwU1lUaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1mRWpCTnhwdQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy1VSjVjd21ZcQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1WZDlKSU1Pcg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy00QmRCbDhJeg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC03UThiU3hqQg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1tQVE4aHNkMw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy13Q1ZqdDhNWQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy04SzJiZEIySw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1FSjhiVVl2Vw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1jdktTMlNRQw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC01UElyN0w3dg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi1Rc3FZMm5DNQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS1zbmRGM3B2Ug.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMWZlYmUzNmUyMTNfWVgwdFIyNzVKaC1mOFNCZDE2OA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC1zYzdCcG1UeA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC1FaURJZ20wdQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi0yWHVxUUJWcA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1TZEZscFpRVQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS1lakV6cGFEZA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ5MzlkNWYxMzhfbko4VUI5RzNLZi1WOXRyTVljSg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS1NejJGS2YwOA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMWZlYmUzNmUyMTNfWVgwdFIyNzVKaC1EMEhUVXdtMw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi1DN1A5cmlSeg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS1jUnBuSllQcA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkyN2Y2MDdjZjhfWEpIcG5LamtQdi0ydk51RDdoeA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkyN2Y2MDdjZjhfWEpIcG5LamtQdi1UMUF6bXJnYg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1WWmpWc0pncA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS1RenVZT2UyaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA3ZGI0MDY3YWJfVzk5dGI3TG1HaC1TSXdaSXB2bQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi1LSUVITUVGSQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi11Vlc0TnBEaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODBhNDlmNTE5OTZfd2czWlA3VXhrRi05U1YzRGJCYQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1OQmxBUlAwaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS0zWWlJQXZtbA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS10Z2NvVEtOVg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS13S0NaYndvcw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ2OGZkMDUwZWFfVWxXdFpMdUxvSi1BSGk5aDhnMQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1QRzc4UlBLNg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS01NlA4Rk01QQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS00T2cwRlRNeQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1Eam81a0NITg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS0yRk51U3hxaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1FZVpGWFhSUA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1xRTdDMzNjMQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1RS1FjNGVBOA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1xTDk1OHI5Vg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS1BSDBJVEJ2OQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS0zczBxU2Zpdw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS1wYlVYYzRqYQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ2OGZkMDUwZWFfVWxXdFpMdUxvSi0zaFhMYzFIYQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS15N0FiMWw4TA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy1xNXZuNlFPNQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy1qMkNBcjlmVQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy1LYUpld3ZwVw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkZDI1ZWRhODU4MDhfQ292MnQzQ1dKQy1xWE1TS080Wg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS01eWRsQVo3Vw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1EWXg5c3FkVQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS12ZmYwalJobA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS00NlZTT1BGYQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1jc29Iakw5WA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1SUUZ6eGM0Mg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMmU5NDRlYmI4MjdfVDBTdW5oU1lMMi14UG42Y01LdA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1CaTBMMGZQTw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1ZR1hxTkZKaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1WalppNDY5VA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1RbkNOdDRmUg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS1JWGlubElHUQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1Qakl0UENjeQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS15bXVxbXlzYQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1yUjBDa09hSg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ2OGZkMDUwZWFfVWxXdFpMdUxvSi1zclVIUk5ISA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ2OGZkMDUwZWFfVWxXdFpMdUxvSi1UV3BKdTRlbw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1jT3JjZUVwNg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1PTFBTTHZ6NQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODQ2OGZkMDUwZWFfVWxXdFpMdUxvSi00UnhWQ3kzVw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS1VVmRnMlczZA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS00c2JxRDQyUA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWEzN2JmMzBfQnhZMm9sNkhPdS02TGd2RUlOOQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1YN2plbDZWNA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS16WWU0WkVqWQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1TMUcwZjluQg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1vSkdpNk5FaQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1vajhSUHBEVw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1oYXFvczRFOQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS11UUpFbmNvZg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1hYTZtbldqdA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1RZmY1bkpERw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1RMnBLRmJMOQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS1iQ01RV0FkUA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS04UFc5ZFZvQQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTE5OWNjNWRlZGVfdVNORGU2aEQ0RC15bkgzcjJFNg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS02MVJ4YXhBag.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1zZTJ6d0Y2Mg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1FMmh2ZFg0YQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1ZdjU5NkVCMg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS1mZE5pS25SYw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1wNHlJS051bA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS03ZUV4S28zWQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS11MU1zVkQydQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS11SFN3TUROWg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1qVjNVTEU0ZA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5YTVhNDY4M2FfbWg3QUFzZmRkTi1XOERncENHSw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS00QmhZVER0Qg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC03NThZQ0Fteg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS00ampYOXRVTQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYTkyZmEwOTdhMGJfYVRvbEgxUTNqMS11V2VOU21FWA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS1uQ2JvdXdEVg.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1sRk9VanhWVA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS11dTl4aGxJcQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjY5MTYwYzQzYjNfcUM0bm04dEFtYS1hYkdSWFdMRw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1hZjZBcnpnZw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODBhNDlmNTE5OTZfd2czWlA3VXhrRi1jNTU2NUtRRw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MDFlMTEwNjVfcG9GeGRHQTNrMy1wY0t1cGxRNA.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMTk2NGIwY2YyMzFfQml3Q1hYTWdvTS0wMVhoNmF6aw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkODA5MzA0ZDQwYzFfMHJJcW4zUWJlOS1nMzdJY3dmMQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjQyYWFkYzY0MDBfSk52TFRINVE1VS15eENZVTVCSQ.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkyN2Y2MDdjZjhfWEpIcG5LamtQdi1RUENLRGV1Zw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkYzI2YTNhMzQyMmZfelNIcktVSDhOUC1qVllIOGZOYw.jpeg",
"http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVkMjkwOTUxNGQ2MTZfcktubGc0Und0bS1ra2hoRVYzMw.jpeg"]


	for x in pics:
		save_data(x,"D://xx/"+x.replace("http://wechatappdev-1252524126.file.myqcloud.com/appeUTy6Ddw5323/image/bW9kdWxlZGVmYXVsdC1wYWdlZGVmYXVsdC11XzVk","").replace(".jpeg",""))
	# f.sort(key= lambda x:int(x[:-4]))
	# for x in f:
	# 	if("m4a" in x):	
	# 		print("file '"+x+"'")
