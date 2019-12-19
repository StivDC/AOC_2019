import math

f = open("intCode_day2.txt", "r")
def getIntCode(f):
	# The cheating way of doing this intCode shit in python 
	for x in f: y = x
	k = list(y.split(","))
	return [int(x) for x in k]

k = getIntCode(f)

# Setting the "1202 Program alarm" state
k[1] = 12
k[2] = 2

def iCodeEval(k):
	k = k[:]
	for i in range(0, len(k), 4):
		if k[i] == 99:
			break
		else:
			a, b, c = k[int(i+3)], k[int(i+1)], k[int(i+2)]
			if k[i] == 1:
				k[a] = k[b] + k[c]
			elif k[i] == 2:
				k[a] = k[b] * k[c]
	return k

print(iCodeEval(k)[0])

# Part 2

for n in range(100):
	for v in range(100):
		k[1], k[2] = n, v
		try:

			if iCodeEval(k)[0] == 19690720:
				print(100 * n + v)
				break
		except IndexError as ex:
			pass