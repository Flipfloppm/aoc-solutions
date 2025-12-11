f = open("input.txt", "r")
lines = f.read().splitlines()
graph = {}
sol = 0

for line in lines:
    key = line[:3]
    nbrs = line[5:]
    nbrs = nbrs.split(" ")
    graph[key] = nbrs

# dfs but we memoize the results based on if we've found fft/dac already
memo = {}

def dfs(curr, path):
    path.append(curr)

    has_fft = "fft" in path
    has_dac = "dac" in path
    state = (curr, has_fft, has_dac)

    if state in memo:
        path.pop()
        return memo[state]
            
    if curr == "out":
        if has_fft and has_dac:
            memo[state] = 1
            path.pop()
            return 1
        else:
            memo[state] = 0
            path.pop()
            return 0

    total = 0
    for nbr in graph[curr]:
        total += dfs(nbr, path)
    memo[state] = total
    path.pop()
    return total
sol = dfs("svr", [])
print(memo)
print("Final Solution: ", sol)

