f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
coords = []
for line in lines:
    redCoords = line.split(",")
    coords.append(redCoords)

def area(coord1, coord2):
    l = abs(int(coord1[0]) - int(coord2[0])) + 1
    w = abs(int(coord1[1]) - int(coord2[1])) + 1
    return l * w

for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j:
            continue
        sol = max(sol, area(coords[i], coords[j]))

print("Final solution: ", sol)
    
