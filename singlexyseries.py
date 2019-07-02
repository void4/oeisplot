from math import pi, log, sqrt
from collections import Counter
from random import choice, random, sample
from PIL import Image, ImageDraw
import os
import sys

oeis = [l.strip() for l in open("oeis.txt").readlines() if l.strip()]
print(f"{len(oeis)} sequences loaded")
stats = Counter()

w = h = 128


outdir = "output/"
os.makedirs(outdir, exist_ok=True)


#ATTEMPTS = int(sys.argv[1])
#for attempt in range(ATTEMPTS):
#	sa = choice(oeis).split(",")

def mylog(i):
	if i<0:
		return -log(-i)
	elif i==0:
		return 0
	else:
		return log(i)

miv = -w//2 * 1000000
mav = w//2 * 1000000

#print(miv,mav)

def mylog(v):
	return log(abs(v)+1)

def getSeries(line):
	lst = line.split(",")
	#mylog(1+int(i))
	return lst[0].strip(), [int(i) for i in lst[1:] if i]

len_oeis = len(oeis)

for ITER in range(1000):
	c = Counter()

	name_a = None
	name_b = None

	try:
		for line_ia, line_a in enumerate(sample(oeis, 1)):#[oeis[130]]):#oeis#sample(oeis, 100)
		
			print(f"{line_ia}/{len_oeis}")

			name_a, series_a = getSeries(line_a)

			len_a = len(series_a)
			
			if len_a < 2:
				continue
			
			for line_ib, line_b in enumerate(sample(oeis, 1)):
				
				name_b, series_b = getSeries(line_b)
				
				len_b = len(series_b)

				if len_b < 2:
					continue
				
				shortest = min(len_a, len_b)
				
				tmpseries_a = series_a[:shortest]
				tmpseries_b = series_b[:shortest]
				
				mi_a = min(tmpseries_a)
				ma_a = max(tmpseries_a)
							
				mi_b = min(tmpseries_b)
				ma_b = max(tmpseries_b)
				
				if mi_a == ma_a or mi_b == ma_b:
					continue
				
				for i in range(shortest):
					val_a = tmpseries_a[i]
					val_b = tmpseries_b[i]
					
					try:
						x = round((val_a-mi_a)/(ma_a-mi_a)*(w-1))
						y = round((val_b-mi_b)/(ma_b-mi_b)*(h-1))
						#print(x,y,val_a,val_b)
						c[y*w+x] += 1
					except ZeroDivisionError:
						break
	except KeyboardInterrupt:
		pass

	if len(c) == 0:
		continue
		
	img = Image.new("RGB", (w,h), 0)#(255,255,255))
	for k in c:
		c[k] = log(1+c[k])
		#c[k] = sqrt(c[k])
	#print(c)
	
	mi_c = min(c.values())
	ma_c = max(c.values())

	print(len(c), mi_c, ma_c)
	pixels = 0
	for y in range(h):
		for x in range(w):
			count = c[y*w+x]
			if count == 0:
				continue
				
			if mi_c == ma_c:
				col = 255
			else:
				col = int((count - mi_c) / (ma_c-mi_c) * 255)
			
			"""
			if count % 2 == 0:
				pix = (col,0,0)
			else:
				pix = (0,col,0)
			"""
			pix =  (col,col,col)
			img.putpixel((x,y), pix)
			pixels += 1
	
	# XXX
	if pixels > 25:
		img.save(f"xy/xy_{name_a}_{name_b}.png")

	#print(stats)
