import gen

def distance(v1,v2):			# Calculates Distance between two Vertices
	return round(((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)**0.5,2)

def greedyS(v,S):				# Calculates Closest Distance from some vertex in S
	dlist = []
	for s in S:
		dlist.append((v[0]-s[0])**2+(v[1]-s[1])**2)
	return round(min(dlist)**0.5,2)

def greedy(R):
	S = []
	cost = 0

	for r in R:
		if len(S)>0:
			cost+=greedyS(r,S)
		S.append(r)

	return cost
