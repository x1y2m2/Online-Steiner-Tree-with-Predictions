def rter():
	f = open('terminalspr.txt','r')
	cd = []
	for l in f:
		s = l.split(',')
		cd.append((int(s[0]),int(s[1])))
	f.close()
	f = open('terminals.txt','r')
	ab = []
	for l in f:
		s = l.split(',')
		ab.append((int(s[0]),int(s[1])))
	f.close()
	return (ab,cd)