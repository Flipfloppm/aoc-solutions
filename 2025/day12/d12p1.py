f = open("input.txt", "r")
lines = f.read().splitlines()
graph = {}
sol = 0

for line in lines:
    dimensions_str, shape_counts_str = line.split(":")
    length, height = list(map(int, dimensions_str.split("x")))
    shape_counts_str = shape_counts_str.strip()
    shape_counts = list(map(int, shape_counts_str.split(" ")))

    # check if there's too many squares needed for the blocks so that nothing would fit
    if sum(shape_counts) * 7 > length * height:
        continue

    # adjust to see if we have enough like 3x3 blocks for each thing so it's a trivial case
    adjusted_length = length // 3
    adjusted_height = height // 3

    if adjusted_length * adjusted_height >= sum(shape_counts):
        sol += 1
        continue
    
    # non-trivial case where we'll be cooked
    print("help omg")

print("Final Solution: ", sol)





