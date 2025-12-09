from shapely.geometry import Polygon

"""
Yeah i'm a fraud i looked up how to do polygon raytracing stuff
"""
f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
coords = []
polygon = []
for line in lines:
    redCoords = line.split(",")
    intCoord = [int(redCoords[0]), int(redCoords[1])]
    polygon.append(intCoord)
    coords.append(redCoords)
shape = Polygon(polygon)


def area(coord1, coord2):
    coord1 = (int(coord1[0]), int(coord1[1]))
    coord2 = (int(coord2[0]), int(coord2[1]))
    corners = [(coord1[0], coord1[1]) ,(coord1[0], coord2[1]) ,(coord2[0], coord2[1]) ,(coord2[0], coord1[1])]
    currRectangle = Polygon(corners)
    if not shape.covers(currRectangle):
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
possible_sols.sort()
for i in range(len(possible_sols) - 1, len(possible_sols) - 20, -1):
    print(possible_sols[i])



