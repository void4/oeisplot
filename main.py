from math import pi
from collections import Counter
from random import choice


oeis = [l.strip() for l in open("oeis.txt").readlines()]

stats = Counter()

ATTEMPTS = 100
for a in range(ATTEMPTS):
	sa = choice(oeis).split(",")
	sb = choice(oeis).split(",")
	

	
	a = [int(i) for i in sa[1:] if i]
	b = [int(i) for i in sb[1:] if i]

	la = len(a)
	lb = len(b)

	mi = min(la,lb)

	last = a[mi-1]
	text = ""

	deltas = []
	delta = None
	for i in range(mi-1,0,-1):
		text = str(a[i])+"+"+str(b[i])+"/("+text+")"
		#print(text)
		#print(i,f"{a[i]}+{b[i]}/{last}")
		if last == 0:
			#print("Last == 0")
			stats["l=0"] += 1
			break
		new = a[i] + b[i]/last
		newdelta = abs(new-last)
		#print(last)
		deltas.append(newdelta)
		
		if delta is not None and newdelta > delta:
			#print("Delta increased", newdelta, delta)
			stats["d2>0"] += 1
			break
	else:
		print(sa[0],sb[0])
		print(deltas)
		stats["good"] += 1
		delta = newdelta
		last = new

print(stats)
