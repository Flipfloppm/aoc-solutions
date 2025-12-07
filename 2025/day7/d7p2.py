f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
first_line = lines[0]
dp = {}
for i in range(len(first_line)):
    if first_line[i] == "S":
        dp[(1,i)] = 1
        new_string = lines[1][:i] + '|' + lines[1][i + 1:]
        lines[1] = new_string

for i in range(1, len(lines) - 1):
    for j in range(len(lines[0])):
        print(len(lines[0]), j)
        print(lines[i])
        if lines[i][j] == '|':
            if lines[i + 1][j] == '^':
                if not (j - 1) < 0:
                    dp[(i + 1, j - 1)] = dp.get((i + 1, j - 1), 0) + dp.get((i, j), 0)
                    new_string = lines[i + 1][:j - 1] + '|' + lines[i + 1][j:]
                    lines[i + 1] = new_string

                if not (j + 1) >= len(lines[0]):
                    dp[(i + 1, j + 1)] = dp.get((i + 1, j + 1), 0) + dp.get((i, j), 0)
                    new_string = lines[i + 1][:j + 1] + '|' + lines[i + 1][j + 2:]
                    lines[i + 1] = new_string

            else:
                dp[(i + 1, j)] = dp.get((i + 1, j), 0) + dp.get((i,j))
                new_string = lines[i + 1][:j] + '|' + lines[i + 1][j + 1:]
                lines[i + 1] = new_string

print(dp)
print(lines)
for i in range(len(lines[0])):
    print(dp.get((len(lines) - 1, i), 0))
    sol += dp.get((len(lines) - 1, i), 0)
print("Final solution: ", sol)
