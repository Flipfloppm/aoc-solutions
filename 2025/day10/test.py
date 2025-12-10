import math
from scipy.optimize import linprog

def solve_lp(buttons, targets):
    """
    Solve button press problem using Linear Programming.
    
    Args:
        buttons: List of tuples, each contains counter indices affected
        targets: List of target values for each counter
    
    Returns:
        (lp_solution, rounded_solution, lp_total, rounded_total)
    """
    n_buttons = len(buttons)
    n_counters = len(targets)
    
    # Objective: minimize sum of all button presses
    c = [1] * n_buttons
    
    # Build constraint matrix
    # For each counter, sum of buttons affecting it >= target
    # Convert to: -sum <= -target
    A_ub = []
    b_ub = []
    
    for counter_idx in range(n_counters):
        row = []
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                row.append(-1)
            else:
                row.append(0)
        A_ub.append(row)
        b_ub.append(-targets[counter_idx])
    
    # Solve LP
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, method='highs', bounds=(0, None))
    
    if not result.success:
        print("LP solver failed!")
        return None, None, None, None
    
    lp_solution = result.x
    lp_total = result.fun
    
    # Round up to get integer solution
    rounded_solution = [math.ceil(x) for x in lp_solution]
    rounded_total = sum(rounded_solution)
    
    return lp_solution, rounded_solution, lp_total, rounded_total


def verify_solution(buttons, targets, solution):
    """
    Verify that a solution meets all target requirements.
    """
    n_counters = len(targets)
    counters = [0] * n_counters
    
    for button_idx, presses in enumerate(solution):
        for counter_idx in buttons[button_idx]:
            if counter_idx < n_counters:
                counters[counter_idx] += presses
    
    met = all(counters[i] >= targets[i] for i in range(n_counters))
    return counters, met


# Your problem
buttons = [
    (0,1,2,3,4,6,9),
    (0,1,2,3,5,8,9),
    (2,4,9),
    (1,3,4,5,6),
    (0,1,2,3,5,7,8,9),
    (1,2,3,4,5),
    (4,9),
    (1,2,3,4,5,7,8,9),
    (1,3,4,6),
    (1,3,9),
    (2,6),
    (0,1,2,3,4,6,8)
]

targets = [31, 81, 67, 81, 83, 40, 55, 17, 29, 78]

print("="*70)
print("BUTTON PRESS PROBLEM - LINEAR PROGRAMMING SOLUTION")
print("="*70)
print(f"\nNumber of buttons: {len(buttons)}")
print(f"Number of counters: {len(targets)}")
print(f"\nButtons:")
for i, btn in enumerate(buttons):
    print(f"  Button {i}: {btn}")
print(f"\nTargets: {targets}")

print("\n" + "="*70)
print("SOLVING WITH LINEAR PROGRAMMING...")
print("="*70)

lp_solution, rounded_solution, lp_total, rounded_total = solve_lp(buttons, targets)

if lp_solution is not None:
    print("\n--- LP SOLUTION (continuous/fractional) ---")
    print(f"Total presses: {lp_total:.2f}")
    print("\nButton presses:")
    for i, presses in enumerate(lp_solution):
        if presses > 0.01:  # Only show non-zero
            print(f"  Button {i} {buttons[i]}: {presses:.2f}")
    
    print("\n--- ROUNDED SOLUTION (integers) ---")
    print(f"Total presses: {rounded_total}")
    print("\nButton presses:")
    for i, presses in enumerate(rounded_solution):
        if presses > 0:
            print(f"  Button {i} {buttons[i]}: {presses}")
    
    # Verify rounded solution
    final_counters, met = verify_solution(buttons, targets, rounded_solution)
    print(f"\n--- VERIFICATION ---")
    print(f"Targets:       {targets}")
    print(f"Final counters: {final_counters}")
    print(f"All targets met: {met}")
    
    if met:
        print(f"\n✓ ANSWER: Minimum {rounded_total} button presses (after rounding)")
        print(f"  (LP lower bound: {lp_total:.2f})")
    else:
        print(f"\n⚠️ WARNING: Rounded solution doesn't meet all targets!")
        print("This shouldn't happen with proper rounding up.")
    
    # Show gaps
    print(f"\n--- EXCESS PRESSES PER COUNTER ---")
    for i in range(len(targets)):
        excess = final_counters[i] - targets[i]
        print(f"  Counter {i}: {final_counters[i]} (need {targets[i]}, excess: {excess})")
else:
    print("Failed to solve LP!")
