import csv

import bpy
import math
import bpy
import time
import os

steep_rate=10
number=2

def select(name):
	bpy.ops.object.select_pattern(pattern=str(name))
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]

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

for x in range(20):
	pass
	make_obj("app/obj_files/3dframe"+str(number)+".obj","3dframe"+str(number))

	bpy.ops.object.select_all(action='TOGGLE')


	select("3dframe"+str(number))
	number=number+steep_rate



#bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

#0.25     0.0     0,0   3dframe2
#1.5      8.0     0.0   3dframe12
#2.7      16.0    0.0   3dframe22
#4.0      22.0    0.0   3dframe32
#5.25     0.0     5.0   3dframe42
#8.00     6.5     5.0   3dframe52
#7.75     16.0    5.0   3dframe62
#9.0      22.0    5.0   3dframe72
#10.25    22.0    10.0  3dframe72
#11.50    22.0    0.0   3dframe92
#11.50    22.0    0.0   3dframe92

def loc(name,r) :
	bpy.data.objects[name].location[0] = r[0]
	bpy.data.objects[name].location[1] = r[1]
	bpy.data.objects[name].location[2] = r[2]  

array_y = [0,10,20,30,0,10,20,30,0,10,20,30,0,10,20,30,0,10,20,30]

array_x = [0,0,0,0,20,20,20,20,40,40,40,40,60,60,60,60,80,80,80,80]


number=2
for x in range(20):
	pass
	#make_obj(PATH+""+str(number)+".obj")
	bpy.ops.object.select_all(action='TOGGLE')
	select("3dframe"+str(number))

	l=[float(array_y[x]),float(1.25+x*1.25),float(array_x[x])]

	loc("3dframe"+str(number),l)

	bpy.ops.object.editmode_toggle()
	bpy.context.scene.tool_settings.use_snap = True
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1.4), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
	bpy.ops.object.editmode_toggle()
	number=number+steep_rate



bpy.ops.wm.save_as_mainfile(filepath="app/object.blend")



