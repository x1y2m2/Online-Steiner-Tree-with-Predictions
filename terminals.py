import random
import time

def dis(x,y):
	a = x**2 + y**2
	b = (1000-x)**2 + (1000-y)**2
	c = (1000-x)**2 + y**2
	d = x**2 + (1000-y)**2
	return int((max(a,b,c,d))**0.5)

def terminals():
	f1 = open('terminals.txt','w')
	f2 = open('terminalspr.txt','w')
	
	random.seed()
	
	for i in range(100):
		x = random.randint(0,1000)
		y = random.randint(0,1000)
	
		d = int(dis(x,y)/100)
	
		px = random.randint(x-d,x+d)
		py = random.randint(y-d,y+d)
	
		f1.write(str(x)+','+str(y)+'\n')
		f2.write(str(px)+','+str(py)+'\n')
	
	f1.close()
	f2.close()
