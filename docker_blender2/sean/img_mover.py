f = open("full_rock.txt", "w")
def number_fixer(number):
	if len(str(number))==1:
		return "00"+str(number)
	if len(str(number))==2:
		return "0"+str(number)
	return str(number)
for x in range(600):

	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(-0)+",100,"+str(x)+"\n")
	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(-0.126*x)+",100,"+str(x-1)+"\n")
	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(-0.126*x)+",0,"+str(x)+"\n")
	f.write("l,2d_frame."+str(number_fixer(x))+",0,"+str(-0.126*x)+",100,"+str(x+1)+"\n")

