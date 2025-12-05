f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
foundSplit = False
ranges = []
for line in lines:
    if len(line) == 0:
        foundSplit = True
        continue

    if not foundSplit:
        ingredientRange = line.split("-")
        l, r = int(ingredientRange[0]), int(ingredientRange[1])
        ranges.append((l, r))

    if foundSplit:
        id = int(line)
        for ingredientRange in ranges:
            if id <= ingredientRange[1] and id >= ingredientRange[0]:
                sol += 1
                break
print("Final Solution: ", sol)

        
