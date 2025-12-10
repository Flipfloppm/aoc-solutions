from itertools import permutations

f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
switch_end_states = []
buttons = [[] for i in range(len(lines))]

# first parse through for the end state and the buttons and store them in binary
for j in range(len(lines)):
    line = lines[j]
    for i in range(len(line)):
        if line[i] == "[":
            i += 1
            switch_end_state = ""
            while line[i] != "]":
                if line[i] == "#":
                    switch_end_state += '1'
                else:
                    switch_end_state += '0'
                i += 1
            switch_end_states.append(switch_end_state)
        
        if line[i] == '(':
            i += 1
            button_str = ""
            while line[i] != ')':
                button_str += line[i]
                i += 1
            toggled_switches = button_str.split(",")
            button = ["0" for k in range(len(switch_end_states[j]))]
            for switch in toggled_switches:
                button[int(switch)] = "1"
            button = "".join(button)
            buttons[j].append(button)

# go through permutations to find smallest set that will give us the end result
for i in range(len(switch_end_states)):
    end_state = switch_end_states[i]
    button_set = buttons[i]
    found = False
    for j in range(1, len(button_set) + 1):
        perms = list(permutations(button_set, j))
        for perm in perms:
            button_status = 0
            for button_press in perm:
                button_status = button_status ^ int(button_press, 2)
            if button_status == int(end_state, 2):
                found = True
                break
        if found:
            sol += j
            break
    if not found:
        print("not found")
print(sol)
