import time

def measure_CPU_time(expression):
    t0 = time.perf_counter()
    eval(expression)
    t1 = time.perf_counter()
    return t1-t0 #result in seconds


def climb_combination(n_stairs : int) -> int:
    # Checks if reached n_stairs
    if n_stairs == 0:
        return 1
    # Checks if exceeded n_stairs
    if n_stairs < 0:
        return 0
    # Else: take one more steps
    return climb_combination(n_stairs - 1) + climb_combination(n_stairs - 2)

def climb_combinations_memo(n_stairs : int, mem=None) -> int:
    if mem == None:
        mem = {1:1,2:2}
    if n_stairs in mem:
        return mem[n_stairs]
    mem[n_stairs] = climb_combinations_memo(n_stairs - 1) + climb_combinations_memo(n_stairs - 2)
    return mem[n_stairs]
n_stairs = int(input("Please enter the amount of stairs to calculate: "))
# max_combs = climb_combination(n_stairs)
# print(f'The amount of combinations available for {n_stairs} is {max_combs}')

# max_combo_memo = climb_combinations_memo(n_stairs)
# print(f'The amount of combinations available for {n_stairs} is {max_combo_memo}')
print('normal:')
print(measure_CPU_time('climb_combination(n_stairs)'))
print('memo')
print(measure_CPU_time('climb_combinations_memo(n_stairs)'))