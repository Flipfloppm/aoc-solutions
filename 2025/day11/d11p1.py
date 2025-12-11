f = open("input.txt", "r")
lines = f.read().splitlines()
graph = {}
sol = 0

for line in lines:
    key = line[:3]
    nbrs = line[5:]
    nbrs = nbrs.split(" ")
    graph[key] = nbrs

def dfs(curr):
    global sol
    if curr == "out":
        sol += 1
    else:
        for nbr in graph[curr]:
            dfs(nbr)

dfs("you")
print("Final Solution: ", sol)

