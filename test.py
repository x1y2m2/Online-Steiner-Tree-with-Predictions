import mst_pr
import greedy
import offline
import terminals
import gen

terminals.terminals()

ters = gen.rter()
rr = ters[0]
prter = ters[1]

print('Offline	:	'+str(offline.offline(rr)))
print('Greedy	:	'+str(greedy.greedy(rr)))
print('Online(s):	'+str(mst_pr.on(rr,prter,'standard')))
print('Online(m):	'+str(mst_pr.on(rr,prter,'modified')))