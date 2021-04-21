import os
 
files=os.listdir(r"D:\家园共育-教师课程(1)")
for x in files:
	mp4Files=os.listdir(r"D:\家园共育-教师课程(1)"+"\\"+x)
	for m in mp4Files:
		print("ffmpeg -hwaccel cuvid -c:v h264_cuvid -i "+r"“D:\家园共育-教师课程(1)"+"\\"+x+"\\"+m+"” -c:v h264_nvenc "+r"“D:\家园共育-教师课程(1)"+"\\"+x+"\\_compress"+m+"”")