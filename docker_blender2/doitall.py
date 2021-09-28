import os
import time
from PIL import Image

path, dirs, files = next(os.walk("app/ims"))
file_count = len(files)
if len(files)<=150:
	os.system("blender app/img_base.blend --background --python app/make_img_breaker.py")
	os.system("blender app/myimg_breaker.blend --background -a")
	print("in right place")


	def number_fixer(x):
		if len(str(x))==1:
			return "000"+str(x)
		if len(str(x))==2:
			return "00"+str(x)
		if len(str(x))==3:
			return "0"+str(x)
		return str(x)
	def do_ithelper(file_location,pix0,pix1,pix2,offset,save_loc,numberoffframes):
		def test(pix,x,y):
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

	file_location="app/ims"
	save_loc="app/cleen2/"





	print("ere we go")
	try:
		do_ithelper(file_location,1,1,1,60,save_loc,210 )
		pass
	except:
		print("done")





	def do_it(test,file_location,number_off):


		def get_start(im,pix,test):
			face={0}
			values={"-1,-1":-1}
			count=0
			value=[]
			notface={0}
			for x in range(im.size[0]):
				for y in range(im.size[1]):
					if x!=0 and y!=0 and x!=(im.size[0]-1) and y!=(im.size[1]-1):
						#print(pix[x,y])
						if test(pix,x,y):
							#print("passed")
							values.update( {str(x)+","+str(y) : count} )
							count=count+1
							value.append([x,y])
						else:
							pass
							#print("fail")
			#quit()
			for x in range(len(value)):
				up=values.get(str(value[x][0]+1)+","+str(value[x][1]))
				if up is None:
					up=-1

				upright=values.get(str(value[x][0]+1)+","+str(value[x][1]+1))
				if upright is None:
					upright=-1

				upleft=values.get(str(value[x][0]+1)+","+str(value[x][1]-1))
				if upleft is None:
					upleft=-1

				down=values.get(str(value[x][0]-1)+","+str(value[x][1]))
				if down is None:
					down=-1

				downright=values.get(str(value[x][0]-1)+","+str(value[x][1]+1))
				if downright is None:
					downright=-1

				downleft=values.get(str(value[x][0]-1)+","+str(value[x][1]-1))
				if downleft is None:
					downleft=-1

				left=values.get(str(value[x][0])+","+str(value[x][1]-1))
				if left is None:
					left=-1

				right=values.get(str(value[x][0])+","+str(value[x][1]+1))
				if right is None:
					right=-1

				uleft=check(up,left,x,face)
				if uleft!=0:
					if uleft not in notface:
						notface.add(check(x,left,upleft,notface))
						notface.add(check(x,up  ,upleft,notface))
						face.add(uleft)

				uright=check(up,right,x,face)
				if uright!=0:
					if uright not in notface:
						notface.add(check(x,right,upright,notface))
						notface.add(check(x,up   ,upright,notface))
						face.add(uright)

				dleft=check(down,left,x,face)
				if dleft!=0:
					if dleft not in notface:
						notface.add(check(x,left,downleft,notface))
						notface.add(check(x,down,downleft,notface))
						face.add(dleft)

				dright=check(down,right,x,face)
				if dright!=0:
					if dright not in notface:
						notface.add(check(x,right,downright,notface))
						notface.add(check(x,down,downright,notface))
						face.add(dleft)

			return [value,face]




		def check(val1,val2,val3,sets):
			#print(sets)
			#print(val1,val2,val3)
			if val1!=-1 and val2!=-1 and val3!=-1:
				val1=val1+1
				val2=val2+1
				val3=val3+1

				if val1>=val2 and val1>=val3:
					if val3>=val2:
						val=str(val1)+","+str(val3)+","+str(val2)
					else:
						val=str(val1)+","+str(val2)+","+str(val3)
					if val not in sets:
						return val
				

				if val2>=val1 and val2>=val3:
					if val3>=val1:
						val=str(val2)+","+str(val3)+","+str(val1)
					else:
						val=str(val2)+","+str(val1)+","+str(val3)
					if val not in sets:
						return val

				if val3>=val1 and val3>=val2:
					if val2>=val1:
						val=str(val3)+","+str(val2)+","+str(val1)
					else:
						val=str(val3)+","+str(val1)+","+str(val2)
					if val not in sets:
						return val
			return 0



					
					
		def value_fixer(values):
			new_value=[]
			for x in range(values):
				pass


		def number_fixer(x):
			if len(str(x))==1:
				return "000"+str(x)
			if len(str(x))==2:
				return "00"+str(x)
			if len(str(x))==3:
				return "0"+str(x)
			return str(x)

		def wright_(values,stl,value):
			f = open(stl+".obj", "w")
			#face=faces_(values)
			for x in range(len(values[0])):
				f.write("v "+str(values[0][x][0]/100)+" "+str(values[0][x][1]/100) +" "+str(value/8)+"\n")
			#print(values[1])
			#print(values[1])
			for mace in values[1]:
				if mace!=0:
					mace=mace.split(",")
					#print("f "+mace[0]+"//1 "+mace[1]+"//1 "+mace[2]+"//1\n")
					f.write("f "+mace[0]+"//1 "+mace[1]+"//1 "+mace[2]+"//1\n")
			f.close()
		number=2
		for x in range(number_off):
			print("go",number)


			im = Image.open('app/cleen2/cleen_V2_'+number_fixer(number)+'.png') # Can be many different formats.
			pix = im.load()
			print(im.size)  # Get the width and hight of the image for iterating over
			print(pix[1,1])  # Get the RGBA Value of the a pixel of an image

			around=get_start(im,pix,test)

			wright_(around,"app/obj_files/3dframe"+str(number),number)
			number=number+1


		im = Image.open(file_location+'/00'+str(20)+'.png')
		pix = im.load()

		for x in range(im.size[0]):
			for y in range(im.size[1]):
				pass

				print(test(pix,x,y))
				#print(pix[x,y])
				print(test(pix,x,y))
				print(pix[x,y])
		#quit()

	def do_ithelper(file_location,pix0,pix1,pix2,offset,number_off):
		def test(pix,x,y):
			# and pix[x,y][0]>=160 and pix[x,y][1]>=40 and pix[x,y][1]<=70 and pix[x,y][2]>=1):
			return not (pix[x,y][0]==255 and pix[x,y][1]==255 and pix[x,y][2]==255 and pix[x,y][3]==0 )
		do_it(test,file_location,number_off)

	import os
	file_location="/cleen2"
	im = Image.open("app/ims/0002.png")
	pix = im.load()

	# change last arg
	try:
		do_ithelper(file_location,pix[0,0][0],pix[0,0][1],pix[0,0][2],0,600)
		pass
	except:
		pass




	os.system("blender app/blank.blend --background --python app/done.py")
else:
	os.system("cp -r app/cleen2 app/sapp/cleen2")
	os.system("blender app/working_2.blend --background --python app/insert_and_extrude.py")





quit()


# C:\Users\Andy\Desktop\blender-2.79-windows64>blender.exe