import time

def measure_CPU_time(expression):
    t0 = time.perf_counter()
    eval(expression)
    t1 = time.perf_counter()
    return t1-t0 #result in seconds

def catalan(c: int) -> int:
    res = 0
    if c <= 1:
        return 1
    for next_val in range(c):
        for next_val2 in range(c):
            sum_vals = next_val + next_val2

            if sum_vals == (c-1):
                res += (catalan(next_val) * catalan(next_val2))
    return res
        

def catalan_memo(c: int, memo = None) -> int:
    if memo == None:
        memo = {0:1, 1:1}
    res = 0

    if c in memo:
        return memo[c]

    for next_val in range(c):
        for next_val2 in range(c):
            sum_vals = next_val + next_val2

            if sum_vals == (c-1):
                if next_val not in memo:
                    memo[next_val] = catalan_memo(next_val)
                if next_val2 not in memo:
                    memo[next_val2] = catalan_memo(next_val2)
                res += memo[next_val] * memo[next_val2]
    return res
main_c = int(input('Enter n : '))
print(measure_CPU_time('catalan(main_c)'))
print(measure_CPU_time('catalan_memo(main_c)'))
