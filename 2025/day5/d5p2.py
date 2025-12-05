"""
ts do not work lol
"""
f = open("input2.txt", "r")
sol = 0
lines = f.read().splitlines()
foundSplit = False
rangeStack = []
for line in lines:
    ingredientRange = line.split("-")
    l,r = int(ingredientRange[0]), int(ingredientRange[1])
    not_found = True
    print(l,r)

    toRemove = []
    for i in range(len(rangeStack)):
        print("Start", rangeStack)
        print(i)
        currRange = rangeStack[i]
        print((l,r), currRange)
        l_in_range = l >= currRange[0] and l <= currRange[1]
        r_in_range = r >= currRange[0] and r <= currRange[1]

        if l_in_range:
            not_found = False
            rangeStack[i] = (currRange[0], max(r, currRange[1]))
            idx = 1
            while True and i+idx < len(rangeStack):
                nextRange = rangeStack[i + idx]
                r_in_next_range = r >= nextRange[0] and r <= nextRange[1]
                if r_in_next_range:
                    toRemove.append(i+idx)
                    rangeStack[i] = (currRange[0], max(r, nextRange[1]))
                idx += 1


        elif r_in_range:
            not_found = False
            rangeStack[i] = (min(l, currRange[0]), currRange[1])
            idx = 1
            toRemove = []
            while True and i-idx > -1:
                nextRange = rangeStack[i - idx]
                l_in_next_range = l >= nextRange[0] and l <= nextRange[1]
                if l_in_next_range:
                    toRemove.append(i-idx)
                    rangeStack[i] = (min(l, nextRange[0]), currRange[1])
                idx += 1

    for i in range(len(toRemove) - 1, -1, -1):
        rangeStack.pop(toRemove[i])
    if not_found:
        rangeStack.append((l,r))
    rangeStack.sort()

    if len(rangeStack) == 0:
        rangeStack.append((l,r))
    print(rangeStack)

        

            

print(rangeStack)
for r in rangeStack:
    sol += r[1] - r[0] + 1

print("Final Solution: ", sol)

