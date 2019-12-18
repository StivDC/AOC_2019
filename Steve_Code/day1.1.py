import math

f = open("fuel.txt", "r")
k = []

def gFuel(x):
	# Use my code KEEMSTAR for 5% off GFUEL
	return math.floor(int(x) / 3 - 2)

for x in f:
	y = 0
	while gFuel(x) >= 0:
		y += gFuel(x)
		x = gFuel(x)
	k.append(y)

print(sum(k))