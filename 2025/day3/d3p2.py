f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
for line in lines:
    jolts = ""
    prev_largest = (-1, -1)
    for i in range(12):
        # each iteration we find the largest from prevFoundIdx + 1 to len(line) - (12 - i) because we need to account for the rest 
        # of the jolt digits that we haven't found yet
        end_idx = len(line) - (12 - i) + 1
        temp_largest = (-1, -1)
        # print("start: ", prev_largest[1] + 1, ", end: ", end_idx )
        for j in range(prev_largest[1] + 1, end_idx):
            if int(line[j]) > temp_largest[0]:
                temp_largest = (int(line[j]), j)
                prev_largest = temp_largest
        jolts += str(temp_largest[0])
        # print(jolts)
    sol += int(jolts)

print("Final Solution: ", sol)


