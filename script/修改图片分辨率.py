import glob as glob
import PIL.Image as Image
import os



def handler(path,hz1,hz2,root,index):
	im = Image.open(path)
	print(im.size)
	w=im.size[0]
	h=im.size[1]
	ww=750
	hh=h/(w/ww)
	print(ww,hh)
	im.thumbnail((ww,hh))
	print(im.format, im.size, im.mode)
	im.save(root+"turn_temp_"+str(index)+".jpg",hz2)

if __name__ == '__main__':
	root="C:/Users/Administrator/Desktop/static/"
	for index,x in enumerate(os.listdir(root)):
		handler(root+x,"jpg","JPEG",root,index)
		# handler(root+x+"/","png","png")
