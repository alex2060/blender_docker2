f = open("img_fram_mover.txt", "w")


def number_fixer(number):
	if len(str(number))==1:
		return "00"+str(number)
	if len(str(number))==2:
		return "0"+str(number)
	return str(number)
for x in range(210):
	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(0.88875*x+0.5)+",100,"+str(x-1)+"\n")
	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(0.88875*x+0.5)+",0,"+str(x)+"\n")
	if ((x-2)%15)==0:
		f.write("l,2d_frame."+str(number_fixer(x))+",-150,"+str(0.88875*x+0.1)+",0,"+str(x+75)+"\n")
	else:
		f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(0.88875*x+0.1)+",100,"+str(x+1)+"\n")


print("done")

