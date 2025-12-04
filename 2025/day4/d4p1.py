f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
# generate the matrix
mat = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    mat.append(row)

dir = [(-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == '.':
            continue
        c = 0
        valid = True
        for dr, dc in dir:
            new_i = i + dr
            if new_i < 0 or new_i >= len(mat):
                continue
            new_j = j + dc
            if new_j < 0 or new_j >= len(mat[0]):
                continue
            if mat[new_i][new_j] == '@':
                c += 1
            if c > 3:
                valid = False
                break

        if valid:
            sol += 1

print("Final Solution: ", sol)
