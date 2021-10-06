import os
import time
from PIL import Image
import os


print("start")
def make_file_obj(herewego,output):
	im = Image.open(herewego)
	pix = im.load()
	contstuctor=[0]*960
	for x in range(960):
		contstuctor[x]=[0]*540
		for y in range(540):
			if pix[x,y]==(255,255,255,0):
				pass
			else:
				contstuctor[x][y]=1

	def check_if_we_are_good(array,x_spot,y_spot):
		faces = [0]*4
		faces[1] = [x_spot+0,y_spot+0]
		faces[0] = [x_spot+9,y_spot+0]
		faces[2] = [x_spot+9,y_spot+9]
		faces[3] = [x_spot+0,y_spot+9]
		for x in range(10):
			for y in range(10):
				if array[x_spot+x][y_spot+y]!=1:
					return [array,False]
		for x in range(8):
			for y in range(8):
				array[x_spot+x+1][y_spot+y+1]=0


		return [array,faces]


	def check_if_we_are_good2(array,x_spot,y_spot):
		faces = [0]*4
		faces[1] = [x_spot+0,y_spot+0]
		faces[0] = [x_spot+4,y_spot+0]
		faces[2] = [x_spot+4,y_spot+4]
		faces[3] = [x_spot+0,y_spot+4]
		for x in range(5):
			for y in range(5):
				if array[x_spot+x][y_spot+y]!=1:
					return [array,False]
		for x in range(3):
			for y in range(3):
				array[x_spot+x+1][y_spot+y+1]=0


		return [array,faces]

	def check_if_we_are_good3(array,x_spot,y_spot):
		faces = [0]*4
		faces[1] = [x_spot+0,y_spot+0]
		faces[0] = [x_spot+2,y_spot+0]
		faces[2] = [x_spot+2,y_spot+2]
		faces[3] = [x_spot+0,y_spot+2]
		for x in range(3):
			for y in range(3):
				if array[x_spot+x][y_spot+y]!=1:
					return [array,False]
		for x in range(1):
			for y in range(1):
				array[x_spot+x+1][y_spot+y+1]=0


		return [array,faces]

	faces = []




	for x in range(47*2):
		for y in range(26*2):
			checker= check_if_we_are_good(contstuctor,9*x,9*y)
			contstuctor=checker[0]
			if checker[1]!=False:
				faces.append(checker[1])



	for x in range(47*2*2):
		for y in range(26*2*2):
			checker= check_if_we_are_good2(contstuctor,4*x,4*y)
			contstuctor=checker[0]
			if checker[1]!=False:
				faces.append(checker[1])



	for x in range(156*3 ):
		for y in range(85*3):
			checker= check_if_we_are_good3(contstuctor,2*x,2*y)
			contstuctor=checker[0]
			if checker[1]!=False:
				faces.append(checker[1])




	for x in range(len(contstuctor)):
		for y in range(len(contstuctor[0]) ):
			if contstuctor[x][y]==1 and contstuctor[x+1][y+0]==1 and contstuctor[x+1][y+1]==1 and contstuctor[x+0][y+1]==1:
				faces.append([ [x+1,y+0],[x+0,y+0],[x+1,y+1],[x+0,y+1] ] )



	counter=[0]*960
	for x in range(960):
		counter[x]=[0]*540


	f = open( output, "w")


	for x in range(960):
		for y in range(540 ):
			if contstuctor[x][y]==2:
				pass
				f.write("v "+str(x/100)+" "+str(y/100)+" 2\n")
			if contstuctor[x][y]==1:
				f.write("v "+str(x/100)+" "+str(y/100)+" 1\n")

	mycounter = 1
	for x in range(960):
		for y in range(540):
			if contstuctor[x][y]!=0:
				counter[x][y]=mycounter
				mycounter=mycounter+1



	for x in range(len(faces)):
		valueC1= str(  counter[faces[x][0][0] ][faces[x][0][1] ]  ) +"//1"
		valueC2= str(  counter[faces[x][1][0] ][faces[x][1][1] ]  ) +"//1"
		valueC3= str(  counter[faces[x][2][0] ][faces[x][2][1] ]  ) +"//1"
		valueC4= str(  counter[faces[x][3][0] ][faces[x][3][1] ]  ) +"//1"
		f.write( "f "+valueC2+" "+valueC1+" "+valueC3+" "+valueC4+"\n" )
		#quit()


		#array_of_values[x]=counter[ faces[0][x][0] ][ faces[0][x][1] ]

	f.close()

def number_fixer(x):

	if len(str(x))==1:
		return "000"+str(x)
	if len(str(x))==2:
		return "00"+str(x)
	if len(str(x))==3:
		return "0"+str(x)
	return str(x)

def do_ithelper(file_location,pix0,pix1,pix2,offset,save_loc,numberoffframes):
	def tesfinhereinheret(pix,x,y):
		return not (pix[x,y][0]<=pix0+offset and pix[x,y][0]>=pix0-offset and pix[x,y][1]<=pix1+offset and pix[x,y][1]>=pix1-offset and pix[x,y][2]<=pix2+offset and pix[x,y][2]>=pix2-offset)
	number=2
	for x in range(numberoffframes):
		print("go")
		im = Image.open('app/ims/'+number_fixer(number)+'.png') # Can be many different formats.
		im = im.convert("RGBA")
		pix = im.load()
		print(im.size)  # Get the width and hight of the image for iterating over
		print(pix[1,1])  # Get the RGBA Value of the a pixel of an image
		pix0=pix[0,0][0]
		pix1=pix[0,0][1]
		pix2=pix[0,0][2]
		width, height = im.size
		#(hight,width,"hight,width")
		for y in range(height):
			for x in range(width):
				if (pix[x,y][0]<=pix0+offset and pix[x,y][0]>=pix0-offset and pix[x,y][1]<=pix1+offset and pix[x,y][1]>=pix1-offset and pix[x,y][2]<=pix2+offset and pix[x,y][2]>=pix2-offset):
					pix[x, y] = (255, 255, 255, 0)

		im.save(save_loc+"cleen_V2_"+number_fixer(number)+".png", "PNG")
		print(save_loc+"cleen_"+number_fixer(number)+".png")
		print("saved")

		#wright_(around,"myframe"+str(number),number)
		number=number+1

	#do_it(test,file_location)


path, dirs, files = next(os.walk("app/ims"))

file_count = len(files)
print(files)
print(dirs)


if file_count<=150:
	os.system("blender app/img_base.blend --background --python app/make_img_breaker.py")
	os.system("blender app/myimg_breaker.blend --background -a")
	print("in right place")

	file_location="app/ims"
	save_loc="app/app/cleen2/"
	do_ithelper(file_location,1,1,1,60,save_loc,209 )

	# change last arg
	number = 2
	for x in range(209):
		print("made",x)
		make_file_obj("app/app/cleen2/cleen_V2_"+number_fixer(number)+".png","app/obj_files/3dframe"+str(number)+".obj")
		number=number+1
	#a =asdfdasfasdfa


	os.system("blender app/blank.blend --background --python app/done.py")
else:
	os.system("cp -r app/cleen2 app/sapp/cleen2")
	os.system("blender app/working_2.blend --background --python app/insert_and_extrude.py")





quit()


# C:\Users\Andy\Desktop\blender-2.79-windows64>blender.exe