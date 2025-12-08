import math
from collections import deque
f = open("input.txt", "r")
sol = 1
lines = f.read().splitlines()
coords = []
distance_map = {}
for line in lines:
    coord = line.split(",")
    coords.append(coord)

def dist(coord1, coord2):
    x = (int(coord2[0]) - int(coord1[0])) ** 2
    y = (int(coord2[1]) - int(coord1[1])) ** 2
    z = (int(coord2[2]) - int(coord1[2])) ** 2
    return math.sqrt(x + y + z)

graph = {}
# get distances 
for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j:
            continue
        distance = dist(coords[i], coords[j])
        if distance in distance_map:
            distance_map[distance].append((coords[i], coords[j]))
        else:
            distance_map[distance] = [(coords[i], coords[j])]
print(distance_map)
distance_keys = list(distance_map.keys())
distance_keys.sort()
print(distance_keys)

NUMBER_OF_PAIRS = 1000

while NUMBER_OF_PAIRS > 0:
    print(NUMBER_OF_PAIRS)
    min_dist = distance_keys[0]
    coord1, coord2 = distance_map[min_dist].pop()
    if len(distance_map[min_dist]) == 0:
        del distance_map[min_dist]
        del distance_keys[0]


    if (tuple(coord1) in graph):
        if tuple(coord2) in graph[tuple(coord1)]:
            continue
        graph[tuple(coord1)].append(tuple(coord2))
    else:
        graph[tuple(coord1)] = [tuple(coord2)]

    if (tuple(coord2) in graph):
        if tuple(coord1) in graph[tuple(coord2)]:
            continue
        graph[tuple(coord2)].append(tuple(coord1))
    else:
        graph[tuple(coord2)] = [tuple(coord1)]
    NUMBER_OF_PAIRS -= 1

# now we traverse the graph to find the longest circuits
circuit_lens = []
visited = set()
def bfs(coord):
    if tuple(coord) in visited:
        return

    circuit_len = 0

    q = deque()
    visited.add(tuple(coord))
    q.append(tuple(coord))
    print("===")

    while q:
        curr = q.popleft()
        circuit_len += 1
        print(curr, circuit_len)

        for nbr in graph[tuple(curr)]:
            if not nbr in visited:
                visited.add(tuple(nbr))
                q.append(tuple(nbr))


    print("===")
    circuit_lens.append(circuit_len)
    return

for coord in graph:
    bfs(coord)

circuit_lens.sort()
print(circuit_lens)

for i in range(len(circuit_lens) - 1, len(circuit_lens) - 4, -1):
    print(circuit_lens[i])
    sol *= circuit_lens[i]

print("Final solution: ", sol)

