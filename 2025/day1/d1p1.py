f = open("input.txt", "r")
dial = 50
sol = 0
for line in f:
    direction = line[0]
    spinAmt = int(line[1:])
    if direction == "L":
        spinAmt = -spinAmt
    print(direction, spinAmt)
    dial += spinAmt
    dial = dial % 100
    print(dial)
    if dial == 0:
        sol += 1
print("Final Result: ", sol)
    
    
