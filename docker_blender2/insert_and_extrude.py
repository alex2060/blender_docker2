import csv

import bpy
import math
import bpy
import time
import os
f = open("/app/sean/base_data_file.txt", "r")
vals=[0]*5
couter=0
for x in f:
  print(x)
  output=x.split(",")
  vals[couter]=output[1].strip("\n")
  couter=couter+1
print(vals)
#quit()
NUMBER_OF_FRAMES=208


PATH ="app/obj_files/3dframe"
thetime=0
number_of_interations=35
steep_rate=int(vals[1])
offset=float(vals[2])
startnumber=2+number_of_interations*steep_rate*thetime
def select(name):
	bpy.ops.object.select_pattern(pattern=str(name))
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]


def make(name,stl,location):
	bpy.ops.import_mesh.obj(filepath=location+str(stl)+"")
	bpy.context.object.name = str(name) 

def make_obj(path,objname):
	file_loc = path
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] ####<--Fix
	print('Imported name: ', obj_object.name)
	bpy.context.scene.objects.active = bpy.data.objects[objname]
	activeObject = bpy.context.active_object
	mat = bpy.data.materials.new(name=str(objname))
	activeObject.data.materials.append(mat)
	bpy.context.object.active_material.name = objname
	bpy.context.object.active_material.name = objname


number=2
for x in range(number_of_interations):
	pass
	make_obj(PATH+""+str(number)+".obj","3dframe"+str(number))

	bpy.ops.object.select_all(action='TOGGLE')


	select("3dframe"+str(number))
	#bpy.ops.object.editmode_toggle()
	#bpy.ops.mesh.select_all(action='TOGGLE')

	#bpy.context.scene.tool_settings.use_snap = True
	#bpy.ops.object.editmode_toggle()
	#bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, offset), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
	#bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(-7.10543e-015, -7.10543e-015, 1), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
	#bpy.ops.object.editmode_toggle()
	#bpy.ops.object.editmode_toggle()
	number=number+steep_rate



#bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
number=2
for x in range(number_of_interations):
	pass
	#make_obj(PATH+""+str(number)+".obj")
	bpy.ops.object.select_all(action='TOGGLE')
	select("3dframe"+str(number))
	bpy.ops.object.editmode_toggle()
	bpy.context.scene.tool_settings.use_snap = True
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, offset), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
	bpy.ops.object.editmode_toggle()
	number=number+steep_rate



import csv
import bpy
import math
import bpy
import time


def check(name):
	heck=1
	try :
		bpy.data.objects[str(name)]
	except:
		heck=0
	return heck
def makerode(points,name,bev,res):
	import bpy
	import math
	import pdb
	from mathutils import Vector
	coords=[""]*len(points)
	for x in range(len(points)):
		coords[x]=points[x]


	# create the Curve Datablock
	curveData = bpy.data.curves.new(name, type='CURVE')
	curveData.dimensions = '3D'
	curveData.resolution_u = 2

	# map coords to spline
	polyline = curveData.splines.new('POLY')
	polyline.points.add(len(coords)-1)
	for i, coord in enumerate(coords):
	    x,y,z = coord
	    polyline.points[i].co = (x, y, z, 1)

	# create Object
	curveOB = bpy.data.objects.new(name, curveData)
	curveData.bevel_depth = bev
	curveData.fill_mode = 'FULL'
	curveData.bevel_resolution = res



	# attach to scene and validate context
	scn = bpy.context.scene
	scn.objects.link(curveOB)
	scn.objects.active = curveOB
def vec(name,end,start) :
	k=[""]*3
	c=[""]*3
	t=[""]*3
	t[0]=start[0]
	t[1]=start[1]
	t[2]=start[2]
	c[0]=end[0]
	c[1]=end[1]
	c[2]=end[2]
	k[0]=c[1]
	k[1]=c[0]
	k[2]=c[2]
	k[1]=k[1]-t[0]
	k[0]=k[0]-t[1]
	k[2]=k[2]-t[2]
	c=k
	h=[c[0],c[1],c[2]]
	lit=c[1]
	
	if c[1]!=0 or c[2]!=0 or c[0]!=0:

		if c[1]!=0 and c[0]!=0:
			thata=math.pi/2-math.atan(c[1]/c[0])
		if c[1]==0 or c[0]==0:
			thata=0
		pi=math.pi/2-math.acos(c[2]/math.sqrt(c[0]**2+c[1]**2+c[2]**2))

		rect=[c[1]/2,c[0]/2,c[2]/2]
##where to change arrow lanth
		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/8
	if c[1]==0 and c[2]==0 and c[0]==0:
		scail=0

	#good
	if c[1]>=0 and c[1]>=0:
		pi=pi
		thata=thata

	if c[0]<=0 and c[1]>=0:
		pi=pi
		thata=thata
	if c[0]>=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	#good
	if c[0]<=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	if c[1]==0:
	    if c[0]>=0:
	        thata=-math.pi/2
	    if c[0]<=0:
	        thata=math.pi/2
	if c[0]==0:
	    if c[1]>=0:
	        thata=0
	    if c[1]<=0:
	        thata=math.pi
	thata=thata
	if c[0]<=0 and c[1]<=0:
		thata=thata+math.pi
	if c[0]>=0 and c[1]>=0:
		thata=thata+math.pi
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h

def vecc(name,end,start) :
	print("this is")
	k=[""]*3
	c=[""]*3
	t=[""]*3
	t[0]=start[0]
	t[1]=start[1]
	t[2]=start[2]
	c[0]=end[0]
	c[1]=end[1]
	c[2]=end[2]
	k[0]=c[1]
	k[1]=c[0]
	k[2]=c[2]
	k[1]=k[1]-t[0]
	k[0]=k[0]-t[1]
	k[2]=k[2]-t[2]
	c=k
	h=[c[0],c[1],c[2]]
	lit=c[1]
	
	if c[1]!=0 or c[2]!=0 or c[0]!=0:

		if c[1]!=0 and c[0]!=0:
			thata=math.pi/2-math.atan(c[1]/c[0])
		if c[1]==0 or c[0]==0:
			thata=0
		pi=math.pi/2-math.acos(c[2]/math.sqrt(c[0]**2+c[1]**2+c[2]**2))

		rect=[c[1]/2,c[0]/2,c[2]/2]

		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/8
	if c[1]==0 and c[2]==0 and c[0]==0:
		scail=0

	#good
	if c[1]>=0 and c[1]>=0:
		pi=pi
		thata=thata

	if c[0]<=0 and c[1]>=0:
		pi=pi
		thata=thata
	if c[0]>=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	#good
	if c[0]<=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	if c[1]==0:
	    if c[0]>=0:
	        thata=-math.pi/2
	    if c[0]<=0:
	        thata=math.pi/2
	if c[0]==0:
	    if c[1]>=0:
	        thata=0
	    if c[1]<=0:
	        thata=math.pi
	thata=thata
	if c[0]<=0 and c[1]<=0:
		thata=thata+math.pi
	if c[0]>=0 and c[1]>=0:
		thata=thata+math.pi
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h

def vec_scail(end,start,sail) :
	k=[""]*3
	c=[""]*3
	t=[""]*3
	t[0]=start[0]
	t[1]=start[1]
	t[2]=start[2]
	c[0]=end[0]
	c[1]=end[1]
	c[2]=end[2]
	k[0]=c[1]
	k[1]=c[0]
	k[2]=c[2]
	k[1]=k[1]-t[0]
	k[0]=k[0]-t[1]
	k[2]=k[2]-t[2]
	c=k
	h=[c[0],c[1],c[2]]
	lit=c[1]
	
	if c[1]!=0 or c[2]!=0 or c[0]!=0:

		if c[1]!=0 and c[0]!=0:
			thata=math.pi/2-math.atan(c[1]/c[0])
		if c[1]==0 or c[0]==0:
			thata=0
		pi=math.pi/2-math.acos(c[2]/math.sqrt(c[0]**2+c[1]**2+c[2]**2))

		rect=[c[1]/2,c[0]/2,c[2]/2]

		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/sail
	if c[1]==0 and c[2]==0 and c[0]==0:
		scail=0

	#good
	if c[1]>=0 and c[1]>=0:
		pi=pi
		thata=thata

	if c[0]<=0 and c[1]>=0:
		pi=pi
		thata=thata
	if c[0]>=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	#good
	if c[0]<=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	if c[1]==0:
	    if c[0]>=0:
	        thata=-math.pi/2
	    if c[0]<=0:
	        thata=math.pi/2
	if c[0]==0:
	    if c[1]>=0:
	        thata=0
	    if c[1]<=0:
	        thata=math.pi
	thata=thata
	if c[0]<=0 and c[1]<=0:
		thata=thata+math.pi
	if c[0]>=0 and c[1]>=0:
		thata=thata+math.pi
	back=[""]*6
	back[0]= rect[0]+t[0]
	back[1] = rect[1]+t[1]
	back[2] = rect[2]+t[2]

	back[3] = scail


	back[4] = -pi
	back[5] = thata+math.pi

	c=h
	return back
def vec(name,end,start) :
	k=[""]*3
	c=[""]*3
	t=[""]*3
	t[0]=start[0]
	t[1]=start[1]
	t[2]=start[2]
	c[0]=end[0]
	c[1]=end[1]
	c[2]=end[2]
	k[0]=c[1]
	k[1]=c[0]
	k[2]=c[2]
	k[1]=k[1]-t[0]
	k[0]=k[0]-t[1]
	k[2]=k[2]-t[2]
	c=k
	h=[c[0],c[1],c[2]]
	lit=c[1]
	
	if c[1]!=0 or c[2]!=0 or c[0]!=0:

		if c[1]!=0 and c[0]!=0:
			thata=math.pi/2-math.atan(c[1]/c[0])
		if c[1]==0 or c[0]==0:
			thata=0
		pi=math.pi/2-math.acos(c[2]/math.sqrt(c[0]**2+c[1]**2+c[2]**2))

		rect=[c[1]/2,c[0]/2,c[2]/2]

		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/8
	if c[1]==0 and c[2]==0 and c[0]==0:
		scail=0

	#good
	if c[1]>=0 and c[1]>=0:
		pi=pi
		thata=thata

	if c[0]<=0 and c[1]>=0:
		pi=pi
		thata=thata
	if c[0]>=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	#good
	if c[0]<=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	if c[1]==0:
	    if c[0]>=0:
	        thata=-math.pi/2
	    if c[0]<=0:
	        thata=math.pi/2
	if c[0]==0:
	    if c[1]>=0:
	        thata=0
	    if c[1]<=0:
	        thata=math.pi
	thata=thata
	if c[0]<=0 and c[1]<=0:
		thata=thata+math.pi
	if c[0]>=0 and c[1]>=0:
		thata=thata+math.pi
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h
#works 
#what it dose is make a arow between 2 points
def get(tpe,life):
	with open(""+tpe+""+life+".txt", "r") as x:
		a1reader=csv.reader(x)
		a1list= []
		for row in a1reader:
			if len(row)!=0:
				a1list=a1list + [row]
		return a1list
	x.close()	 
#works
# get array form csv file
def ges(tpe,life):
	with open(""+tpe+""+life+".txt", "r") as x:
		a1reader=csv.reader(x)
		a1list= []
		for row in a1reader:
			if len(row)!=0:
				a1list=a1list + row
		return a1list
	x.close() 
# gets lift form csv file
def getloc(name):
	a=[""]*3
	a[0]=bpy.data.objects[str(name)].location[0]
	a[1]=bpy.data.objects[str(name)].location[1]
	a[2]=bpy.data.objects[str(name)].location[2]
	return a 
# gets loction of object
def colorset(name):
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]
	activeObject = bpy.context.active_object #Set active object to variable
	mat = bpy.data.materials.new(name=str(name)) 
#def color(name,c):
#	bpy.context.object.active_material.diffuse_color = (0.221483, 0.8, 0.204497)

# looks like it works
# changes collor of object
def loc(name,r) :
	bpy.data.objects[name].location[0] = r[0]
	bpy.data.objects[name].location[1] = r[1]
	bpy.data.objects[name].location[2] = r[2]  
# changes loction of object
def scail(name,s) :
	bpy.data.objects[name].scale[0] = s
	bpy.data.objects[name].scale[1] = s
	bpy.data.objects[name].scale[2] = s 
# scails object
def rot(name,a) :
	bpy.data.objects[name].rotation_euler[0] = a[1]
	bpy.data.objects[name].rotation_euler[1] = a[0]
	bpy.data.objects[name].rotation_euler[2] = a[2]
# rotates object
def make(name,stl,location):
	bpy.ops.import_mesh.stl(filepath=location+str(stl)+"")
	bpy.context.object.name = str(name) 
# makes object given stl
#make("vet","ves.stl")
#"C:/Users/Melinda/Desktop/comp/"
def select1(name):
	bpy.ops.object.select_pattern(pattern=str(name))
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]
# selects an obj by name
# adds objs based on obj_f

#changes angle based on file angle_f
#changes location based on file location_f

#changes scail based on file scail_f

#changes arrows based on file arrow_f

#changes color based on file coolor_f
def scailpartal(name,s):
	bpy.data.objects[name].scale[0] = s[0]
	bpy.data.objects[name].scale[1] = s[1]
	bpy.data.objects[name].scale[2] = s[2]
def stuff(location):
	addobj(location,"All")
def tro(location,fil):
	a=location
	objt=get(location,fil)
	obj=[""]*2
	angle=[""]*4
	location=[""]*4
	se=[""]*2
	sec=[""]*4
	ar=[""]*2
	arw=[""]*9
	coolor=[""]*4
	for x in range(len(objt)):
		frame=objt[x][len(objt[x])-1]
		inpit=0
		try:
			bpy.context.scene.frame_current = int(frame)
		except:
			print("fail"+str(x)+"")
		if objt[x][0]=="o":
			obj[0]=objt[x][1]
			obj[1]=objt[x][2]
			if check(str(obj[0]))==0:
				make(str(obj[0]),str(obj[1]),a)
				#this give the material
				bpy.context.scene.objects.active = bpy.data.objects[str(obj[0])]
				activeObject = bpy.context.active_object
				mat = bpy.data.materials.new(name=str(obj[0]))
				activeObject.data.materials.append(mat)
				bpy.context.object.active_material.name = str(obj[0])
				bpy.context.object.active_material.name = str(obj[0])
		if objt[x][0]=="a":
			angle[0]=objt[x][1]
			angle[1]=objt[x][2]
			angle[2]=objt[x][3]
			angle[3]=objt[x][4]
			try:
				if check(str(angle[0]))==1:
					r=[float(angle[1]),float(angle[2]),float(angle[3])]
					
					rot(str(angle[0]),r)
					bpy.ops.object.select_all(action='DESELECT')
					select(str(angle[0]))
					#bpy.ops.anim.keyframe_insert_menu(type='Rotation')
					bpy.context.object.keyframe_insert("rotation_euler",index=-1, frame=bpy.context.scene.frame_current, group="")
			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="l":
			location[0]=objt[x][1]
			location[1]=objt[x][2]
			location[2]=objt[x][3]
			location[3]=objt[x][4]
			try:
				if check(str(location[0]))==1:
					l=[float(location[1]),float(location[2]),float(location[3])]
					loc(str(location[0]),l)
					bpy.ops.object.select_all(action='DESELECT')
					select(location[0])
					bpy.context.object.keyframe_insert("location",index=-1, frame=bpy.context.scene.frame_current, group="")
			except:
				print("fail"+str(objt[x][0])+"")
		if objt[x][0]=="s":
			se[0]=objt[x][1]
			se[1]=objt[x][2]
			try:
				if check(str(se[0]))==1:
					s=float(se[1])
					scail(str(se[0]),s)
					bpy.ops.object.select_all(action='DESELECT')
					select(se[0])
					#bpy.ops.anim.keyframe_insert_menu(type='Scaling')
					bpy.context.object.keyframe_insert("scale",index=-1, frame=bpy.context.scene.frame_current, group="")
			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="sc":
			sec[0]=objt[x][1]
			sec[1]=objt[x][2]
			sec[2]=objt[x][3]
			sec[3]=objt[x][4]
			try:
				if check(str(sec[0]))==1:
					s=[float(sec[1]),float(sec[2]),float(sec[3])]
					scailpartal(str(sec[0]),s)
					bpy.ops.object.select_all(action='DESELECT')
					select(sec[0])
					bpy.context.object.keyframe_insert("scale",index=-1, frame=bpy.context.scene.frame_current, group="")


			except:
				print("fail"+str(x)+"")

		if objt[x][0]=="ar":
			ar[0]=objt[x][1]
			ar[1]=objt[x][2]
			if check(str(ar[0]))==1 and check(str(ar[1]))==1:
				name=str(ar[0])+"->"+str(ar[1])
				if check(name)==0:
					make(name,"ves.stl",LOC)
					#this give the material
					bpy.context.scene.objects.active = bpy.data.objects[name]
					activeObject = bpy.context.active_object
					mat = bpy.data.materials.new(name=name)
					activeObject.data.materials.append(mat)
					bpy.context.object.active_material.name = name
					bpy.context.object.active_material.name = name
		if objt[x][0]=="arw":
			print("got")
			arw[0]=objt[x][1]# name
			arw[1]=float(objt[x][2])# point1
			arw[2]=float(objt[x][3])
			arw[3]=float(objt[x][4])

			arw[4]=float(objt[x][5])# point 2
			arw[5]=float(objt[x][6])
			arw[6]=float(objt[x][7])
			arw[7]=objt[x][8]# stl
			arw[8]=float(objt[x][9])# lanth
			print(objt[x])
			if check(arw[0])==0:
				make(str(arw[0]),str(arw[7]),LOC)
			starrt=[arw[1],arw[2],arw[3]]
			endds=[arw[4],arw[5],arw[6]]
			vecc(str(arw[0]),starrt,endds)
			print("this")
			select(arw[0])
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			bpy.ops.anim.keyframe_insert_menu(type='Location')


		if objt[x][0]=="c":
			coolor[0]=objt[x][1]
			coolor[1]=objt[x][2]
			coolor[2]=objt[x][3]
			coolor[3]=objt[x][4]
			try:
				if check(str(coolor[0]))==1:
					k=[float(coolor[1]),float(coolor[2]),float(coolor[3])]
					bpy.ops.object.select_all(action='DESELECT')
					select(str(coolor[0]))
					#colorset(str(coolor[0]+"_V1"))
					bpy.context.object.active_material.diffuse_color = (float(coolor[1]), float(coolor[2]), float(coolor[3]))
					bpy.context.object.active_material.keyframe_insert("diffuse_color", index=-1, frame=bpy.context.scene.frame_current, group="")

			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="LH":
			try:
				bpy.ops.object.lamp_add(type='HEMI', radius=1, view_align=False, location=(11.5334, 8.18019, -2.72604), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
			except:
				print("fail"+str(x)+"")


		if objt[x][0]=="select":
			select_P[0]=objt[x][1]
			try:
				if check(str(select_P[0]))==1:
					select(str(select_P[0]))

			except:
				print("fail"+str(x)+"")

		if objt[x][0]=="del":
			#select_P[0]=objt[x][1]
			try:
				select(str(objt[x][1]))
				bpy.ops.object.delete(use_global=False)
			except:
				pass

		if objt[x][0]=="ml":
			number_5=len(objt[x])-5
			number_6=number_5/3
			print(objt)
			pits=[""]*int(number_6)
			print(number_6)
			for k in range(len(pits)):
				pits[k]=[float(objt[x][4+3*k]),float(objt[x][5+3*k]),float(objt[x][6+3*k])]
			print(pits)
			makerode(pits,"the",float(objt[x][2]),float(objt[x][3]))
			

def arrowaddsub(location,arrow_f):
	arw=get(location,arrow_f)
	for x in range(len(arw)):
		if check(str(arw[x][0]))==1 and check(str(arw[x][1]))==1:
			name=str(arw[x][0])+"->"+str(arw[x][1])
			if check(name)==0:
				make(name,"ves.stl",a)
				#this give the material
				bpy.context.scene.objects.active = bpy.data.objects[name]
				activeObject = bpy.context.active_object
				mat = bpy.data.materials.new(name=name)
				activeObject.data.materials.append(mat)
				bpy.context.object.active_material.name = name
				bpy.context.object.active_material.name = name
			dimx=bpy.data.objects[name].dimensions[1]
			dimy=bpy.data.objects[name].dimensions[2]
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			vecs(name,getloc(str(arw[x][0])),getloc(str(arw[x][1])))
			select(str(name))
			bpy.data.objects[name].dimensions[1] = dimx
			bpy.data.objects[name].dimensions[2] = dimy
			bpy.ops.object.select_all(action='DESELECT')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			bpy.ops.anim.keyframe_insert_menu(type='Location')
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')

pits=[""]*3
pits[0]=[0,0,0]
pits[1]=[2,3,4]
pits[2]=[4,3,4]

#bpy.ops.wm.save_as_mainfile(filepath="insert_1.blend")
#quit()

fram1=0
for x in range(75):
	pass
	#bpy.context.scene.frame_set(fram1+x*2)
	#arrowaddsub(LOC,"ves.stl")





Path="app"
last_path="cleen2"
Path=Path+"/"+last_path+"/"
def number_fixer(number):
	if len(str(number))==1:
		return "000"+str(number)
	if len(str(number))==2:
		return "00"+str(number)
	if len(str(number))==3:
		return "0"+str(number)
	return str(number)

def number_fixer2(number):
	if len(str(number))==1:
		return "00"+str(number)
	if len(str(number))==2:
		return "0"+str(number)
	return str(number)






number=2
for x in range(NUMBER_OF_FRAMES):
	select("2d_frame."+number_fixer2(number))
	name="cleen_V2_"+number_fixer(number)
	bpy.ops.image.open(filepath="//cleen2/"+name+".png", files=[{"name":name+".png", "name":name+".png"}], relative_path=True, show_multiview=False)
	bpy.context.object.active_material.node_tree.nodes['Image Texture'].image=bpy.data.images[name+'.png']
	number=number+1
print("img_fram_mover")


tro("","app/sean/img_fram_mover")
tro("","app/sean/background")


tro("","app/sean/object_mover")

bpy.ops.file.autopack_toggle()

tro("","app/sean/light")
tro("","app/sean/camera_mover")
bpy.ops.wm.save_as_mainfile(filepath="app/insert_6.blend")
print("we will save with images")