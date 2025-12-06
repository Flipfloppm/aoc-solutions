f = open("input.txt", "r")
sol = 0
filebody_lines = f.readlines()
symbols = []
valid_symbols = {"*", "+"}
numbers_split = [[[] for j in range(4)] for i in range(len(filebody_lines[0].split()))]
last_found_idx = 0
problems_completed = 0
for i in range(len(filebody_lines[0])):
    num_found = False
    for j in range(5):
        if filebody_lines[j][i] in valid_symbols:
            symbols.append(filebody_lines[j][i])

        if not filebody_lines[j][i].isspace() and filebody_lines[j][i] not in valid_symbols:
            num_found = True
            numbers_split[problems_completed][i - last_found_idx].append(filebody_lines[j][i])

    if not num_found:
        last_found_idx = i + 1
        problems_completed += 1

for i in range(len(numbers_split)):
    problem_sol = 0
    symbol = symbols[i]
    if symbol == "*":
        problem_sol += 1
    for j in range(len(numbers_split[i])):
        if len(numbers_split[i][j]) == 0:
            continue
        if symbol == "*":
            problem_sol *= int("".join(numbers_split[i][j]))
        else:
            problem_sol += int("".join(numbers_split[i][j]))
    sol += problem_sol

print("Final Solution: ", sol)
