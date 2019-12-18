import math

f = open("fuel.txt", "r")

def day1(f):
	return sum([(math.floor(int(x)/3) - 2) for x in f])
print(day1(f))

# l = [math.floor(int(x)/3) - 2 for x in f]
# print(sum(l))