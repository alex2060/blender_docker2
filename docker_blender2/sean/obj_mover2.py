
def number_fixer(number):
	if len(str(number))==1:
		return "00"+str(number)
	if len(str(number))==2:
		return "0"+str(number)
	return str(number)
f = open("object_mover.txt", "w")

for x in range(210):
	offset=str(0.9*x)
	fo=33
	f.write("l,3dframe"+str(x)+",0,"+offset+",-60,"+str(0-fo)+"\n")
	f.write("l,3dframe"+str(x)+",0,"+offset+",0,"+str(x+30-fo)+"\n")
	f.write("l,3dframe"+str(x)+",0,"+offset+",-60,"+str(x+1-fo)+"\n")
	f.write("l,3dframe"+str(x)+",0,"+offset+",-60,"+str(x+105-fo)+"\n")
	
	
	if (x)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")
	if (x+1)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")
	if (x+2)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")
	if (x+3)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")
	if (x+4)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")
	if (x+5)%18==6:
		f.write("c,3dframe"+str(x)+",0.627074,0.01,0.8,"+str(x+15-fo)+"\n")


	if (x)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")
	if (x+1)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")
	if (x+2)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")
	if (x+3)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")
	if (x+4)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")
	if (x+5)%18==12:
		f.write("c,3dframe"+str(x)+",0.234379,0.222435,0.8,"+str(x+15-fo)+"\n")

	if (x)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")

	if (x+1)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")

	if (x+2)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")

	if (x+3)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")

	if (x+4)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")

	if (x+5)%18==0:
		f.write("c,3dframe"+str(x)+",0.89566,0.05,0.13,"+str(x+15-fo)+"\n")
	#if x%4==3:
		#f.write("c,3dframe"+str(x)+",0.9,0.9,0,"+str(x+15)+"\n")
	#if x%4==4:
		#f.write("c,3dframe"+str(x)+",0.9,0,0.9,"+str(x+15)+"\n")
	#f.write("l,3dframe"+str(x)+",0,0,0,"+str(x+105)+"\n")
	#f.write("l,Plane_frame."+number_fixer(x)+",0,-"+str(x*0.125+0.001)+",100,"+str(x+1)+"\n")
f.close()