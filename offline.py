from pcst_fast import pcst_fast
import gen
import numpy as np

def distance(v1,v2):			# Calculates Distance between two Vertices
	return round(((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)**0.5,2)

def edges(vlist,E,ecost):		# Makes a List of Edges
	vlength = len(vlist)
	for i in range(vlength):
		for j in range(i+1,vlength):
			E.append((i,j))
			ecost.append(distance(vlist[i],vlist[j]))

def offline(R):
	E=[]
	ecost=[]
	edges(R,E,ecost)
	vcost=[]
	for i in range(len(R)):
		vcost.append(2000)

	cost=0
	En = np.array(E)
	vv,ee = pcst_fast(E,vcost,ecost,0,1,'strong',0)

	for e in ee:
		cost+=ecost[e]

	return cost

#ters = gen.rter()
#rr = ters[0]
#prter = ters[1]

#print(offline(rr))