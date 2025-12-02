f = open("input.txt", "r")
input = f.read()
input = input[:len(input) - 1]
input = input.split(',')
sol = 0
for ids in input:
    id = ids.split('-')
    l_id = id[0]
    r_id = id[1]
    for i in range(int(l_id), int(r_id) + 1):
        string_id = str(i)
        if not len(string_id) % 2:
            l_half = string_id[0:(len(string_id) // 2)]
            r_half = string_id[len(string_id) // 2:]
            if  l_half == r_half:
                sol += int(string_id)
print("Final solution: ", sol)
