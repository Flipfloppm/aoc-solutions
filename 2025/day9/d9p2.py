from collections import defaultdict
f = open("sample.txt", "r")
sol = 0
lines = f.read().splitlines()
coords = []
for line in lines:
    redCoords = line.split(",")
    coords.append(redCoords)


x_ranges = defaultdict(list)
y_ranges = defaultdict(list)

prev_x, prev_y = coords[0]
prev_x = int(prev_x)
prev_y = int(prev_y)
largest_gap = 0
for i in range(1, len(coords)):
    curr_x, curr_y = coords[i]
    curr_x, curr_y = int(curr_x), int(curr_y)
    if curr_y != prev_y:
        x_ranges[curr_x].append((min(prev_y, curr_y), max(prev_y, curr_y)))
        largest_gap = max(abs(curr_y - prev_y), largest_gap)
    else:
        y_ranges[curr_y].append((min(prev_x, curr_x), max(prev_x, curr_x)))
        largest_gap = max(abs(curr_x - prev_x), largest_gap)

    prev_x = curr_x
    prev_y = curr_y

# for the last entry bc it wraps
curr_x, curr_y = coords[0]
curr_x, curr_y = int(curr_x), int(curr_y)
if curr_y != prev_y:
    x_ranges[curr_x].append((min(prev_y, curr_y), max(prev_y, curr_y)))
    largest_gap = max(abs(curr_y - prev_y), largest_gap)
else:
    y_ranges[curr_y].append((min(prev_x, curr_x), max(prev_x, curr_x)))
    largest_gap = max(abs(curr_x - prev_x), largest_gap)
print(largest_gap)
# we just need a way to check if any point is in the green/red and we can call it on each of the 4 corners

# obvious if it's on the line for anything but how to check if it's between?
# gonna make the assumption that if it's a corner it's on a line and we just need to check if it's in 
# ^ yeah so this assumption was just straight up wrong

                

def isInBoundsX(coord, coord2):
    x, y = int(coord[0]), int(coord[1])
    x2, y2 = int(coord2[0]), int(coord2[1])
    if x in x_ranges:
        for rng in x_ranges[x]:
            if (y <= rng[1] and y >= rng[0]) and (y2 <= rng[1] and y2 >= rng[0]):
                return True
    return False

def isInBoundsY(coord, coord2):
    x, y = int(coord[0]), int(coord[1])
    x2, y2 = int(coord2[0]), int(coord2[1])

    if y in y_ranges:
        for rng in y_ranges[y]:
            if x <= rng[1] and x >= rng[0] and x2 <= rng[1] and x2 >= rng[0]:
                return True

    return False

def area(coord1, coord2):
    corner1 = (coord1[0], coord1[1])
    corner2 = (coord1[0], coord2[1])
    corner3 = (coord2[0], coord1[1])
    corner4 = (coord2[0], coord2[1])

    if not isInBoundsY(corner1, corner3):
        return 0

    if not isInBoundsY(corner2, corner4):
        return 0

    if not isInBoundsX(corner1, corner2):
        return 0

    if not isInBoundsX(corner3, corner4):
        return 0
    l = abs(int(coord1[0]) - int(coord2[0])) + 1
    w = abs(int(coord1[1]) - int(coord2[1])) + 1
    return l * w

possible_sols = []

for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j:
            continue

        temp_area = area(coords[i], coords[j])
        possible_sols.append((temp_area, coords[i], coords[j]))
        # if temp_area > sol:
        #   print(coords[i], coords[j])
        #   sol = temp_area
possible_sols.sort()
for i in range(len(possible_sols) - 1, -1, -1):
    print(possible_sols[i])
