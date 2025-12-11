f = open("sample.txt", "r")
lines = f.read().splitlines()
graph = {}
sol = 0

for line in lines:
    key = line[:3]
    nbrs = line[5:]
    nbrs = nbrs.split(" ")
    graph[key] = nbrs

paths = []
def dfs(curr, path):
    path.append(curr)
    if curr == "out":
        paths.append(path)
    else:
        for nbr in graph[curr]:
            dfs(nbr, path)
    path.pop()

dfs("svr", [])
for path in paths:
    if "fft" in path and "dac" in path:
        sol += 1
print("Final Solution: ", sol)

