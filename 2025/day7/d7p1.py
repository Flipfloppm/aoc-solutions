f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
first_line = lines[0]
for i in range(len(first_line)):
    if first_line[i] == "S":
        new_string = lines[1][:i] + '|' + lines[1][i + 1:]
        lines[1] = new_string

for i in range(1, len(lines) - 1):
    for j in range(len(lines[0])):
        print(len(lines[0]), j)
        print(lines[i])
        if lines[i][j] == '|':
            if lines[i + 1][j] == '^':
                sol += 2
                if not (j - 1) < 0:
                    new_string = lines[i + 1][:j - 1] + '|' + lines[i + 1][j:]
                    lines[i + 1] = new_string

                if not (j + 1) >= len(lines[0]):
                    new_string = lines[i + 1][:j + 1] + '|' + lines[i + 1][j + 2:]
                    lines[i + 1] = new_string

            else:
                new_string = lines[i + 1][:j] + '|' + lines[i + 1][j + 1:]
                lines[i + 1] = new_string


print(lines)
print("Final solution: ", sol)
