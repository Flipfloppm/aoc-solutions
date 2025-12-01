f = open("input.txt", "r")
dial = 50
sol = 0
for line in f:
    direction = line[0]
    spinAmt = int(line[1:])
    if direction == "L":
        for i in range(spinAmt):
            dial -= 1
            dial = dial % 100
            if dial == 0:
                sol += 1
    else:
        for i in range(spinAmt):
            dial += 1
            dial = dial % 100
            if dial == 0:
                sol += 1

print("Final Result: ", sol)
