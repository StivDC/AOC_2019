wire1, wire2 = "", ""
with open("day03input.txt") as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")

direction = {
    "U": (0, 1),
    "D": (0,-1),
    "L": (-1,0),
    "R": (1, 0)
}

def add_tuples(a, b):
    return tuple(map(sum, zip(a, b)))

def mult_tuple(a, s):
    return tuple(s * x for x in a)

def instruction_to_vectors(instruction):
    return [direction[instruction[0]]] * int(instruction[1:])

def walk(path):    
    points = []
    my_pos = (0, 0)

    for instruction in path:
        for vector in instruction_to_vectors(instruction):
            my_pos = add_tuples(my_pos, vector)
            points.append(my_pos)

    return points

path1 = walk(wire1)
path2 = walk(wire2)

# Slooooooooow...........
intersections = [point for point in path1 if point != (0, 0) and point in path2]
# Part 1
print(min(intersections, key = lambda p: abs(p[0]) + abs(p[1])))

# Part 2
intersection_distances = []

# Slooooooooooooower............
for dist1, point1 in enumerate(path1, 1):
    if point1 == (0, 0):
        continue
    
    for dist2, point2 in enumerate(path2, 1):
        if point1 == point2:
            intersection_distances.append(dist1 + dist2)

print(sorted(intersection_distances))