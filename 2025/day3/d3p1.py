f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
for line in lines:
    max1 = (-1, -1)
    # first pass get the largest number and its idx
    for j in range(len(line) - 1):
        if int(line[j]) > max1[0]:
            max1 = (int(line[j]), j)
    max2 = (-1, -1)
    for j in range(max1[1] + 1, len(line)):
        if int(line[j]) > max2[0]:
            max2 = (int(line[j]), j)
    jolts = str(max1[0]) + str(max2[0])
    sol += int(jolts)
        

print("Final Solution: ", sol)


