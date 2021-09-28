import os
import bpy

vals=[0]*5
couter=0


 
bpy.context.scene.render.filepath = "app/ims/"
bpy.context.scene.sequence_editor.sequences.new_movie(filepath="app/video.mp4",channel=1,frame_start=1,name="no_name")
bpy.context.scene.frame_end = 210
bpy.ops.wm.save_as_mainfile(filepath="app/myimg_breaker.blend")
bpy.ops.wm.save_as_mainfile(filepath="app/wesaved2.blend")
#blender -b myimg_breaker.blend -a

