def climb_combination(n_stairs : int) -> int:
    # Checks if reached n_stairs
    if n_stairs == 0:
        return 1
    # Checks if exceeded n_stairs
    if n_stairs < 0:
        return 0
    # Else: take one more steps
    return climb_combination(n_stairs - 1) + climb_combination(n_stairs - 2)

n_stairs = int(input("Please enter the amount of stairs to calculate: "))
max_combs = climb_combination(n_stairs)
print(f'The amount of combinations available for {n_stairs} is {max_combs}')


