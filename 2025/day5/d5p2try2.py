f = open("input2.txt", "r")
sol = 0
lines = f.read().splitlines()
ranges = []
for line in lines:
    ingredient_range = line.split("-")
    l, r = int(ingredient_range[0]), int(ingredient_range[1])
    ranges.append((l,r))

ranges.sort()
i = 0
while i < len(ranges):
    r = ranges[i][1]
    # we find all the ones that r is inside of and move r as we find further
    toRemove = []
    for j in range(i + 1, len(ranges)):
        j_range = ranges[j]
        if r >= j_range[1]:
            toRemove.append(j)
        elif r >= j_range[0] and r <= j_range[1]:
            toRemove.append(j)
            r = j_range[1]
        else:
            break
    ranges[i] = (ranges[i][0], r)
    for i in range(len(toRemove) - 1, -1, -1):
        ranges.pop(toRemove[i])
    i += 1

for l, r, in ranges:
    sol += r - l + 1
print("Final Solution: ", sol)
