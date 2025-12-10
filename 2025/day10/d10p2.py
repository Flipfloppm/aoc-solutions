from scipy.optimize import linprog
import math
f = open("input.txt", "r")
sol = 0
lines = f.read().splitlines()
switch_end_states = []
buttons = [[] for i in range(len(lines))]
button_counters = []

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

        if line[i] == '{':
            i += 1
            counter_str = ""
            while line[i] != '}':
                counter_str += line[i]
                i += 1
            counters = counter_str.split(",")
            button_counters.append(counters)
print(button_counters)
print(buttons)

for i in range(len(button_counters)):
    print("===")
    c = [1 for j in range(len(buttons[i]))]
    print(c)
    print("---")

    # iterate through each counter
    A = []
    b = []
    for j in range(len(button_counters[i])):
        # iterate through each button
        a_sub = []

        for button in buttons[i]:
            if button[j] == '1':
                a_sub.append(-1)
            else:
                a_sub.append(-0)
        A.append(a_sub)
        b.append(-int(button_counters[i][j]))
    print(A)
    print(b)

    result = linprog(c, A_eq=A, b_eq=b, method='highs', integrality=1)
    print("Button presses:", result.x)
    print("Total presses:", result.fun)
    sol += int(result.fun)
print("Final Solution: ", sol)


