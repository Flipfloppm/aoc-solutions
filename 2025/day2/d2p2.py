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
        # now we iterate through 0 to len(str) // 2 and find if the string repeats
        for j in range(1, len(string_id) // 2 + 1):
            string_partial = string_id[:j]
            found = False
            # only check cases where the length divides evenly
            if not len(string_id) % len(string_partial):
                invalid = False
                for k in range(len(string_id) // len(string_partial)):
                    check_str = string_id[len(string_partial) * k: len(string_partial) * (k + 1)]
                    if not check_str == string_partial:
                        invalid = True
                        break
                if not invalid:
                    found = True
                    sol += int(string_id)
                    break





print("Final solution: ", sol)
