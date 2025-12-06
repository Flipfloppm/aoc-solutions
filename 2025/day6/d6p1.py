f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
problems = []
p1_split = lines[0].split()
for i in range(len(p1_split)):
    problems.append([])

for line in lines:
    things = line.split()
    for i in range(len(things)):
        problems[i].append(things[i])

for problem in problems:
    symbol = problem[-1]
    problem_sol = 0
    if symbol == "*":
        problem_sol += 1
    for i in range(len(problem) - 1):
        if symbol == "*":
            problem_sol *= int(problem[i])
        else:
            problem_sol += int(problem[i])
    sol += problem_sol

print("Final Solution: ", sol)
