import time

def measure_CPU_time(expression):
    t0 = time.perf_counter()
    eval(expression)
    t1 = time.perf_counter()
    return t1 - t0

def change(n : int, lst : list) -> int:
    if n == 0:
        return 1
    if lst == []:
        return 0
    coin = lst[0]
    combinations = 0
    if coin <= n:
        combinations += change(n-coin, lst)
    return combinations + change(n, lst[1:])


result = change(4, [1,2,5,7])
print(measure_CPU_time('change(4, [1,2,5,7])'))
print(result)

def change_memo(n : int, lst : list, mem = None) -> int:
    if mem == None:
        mem = {0:1}
    if n == 0:
        return 1
    if lst == []:
        return 0
    coin = lst[0]
    
    first_tmp = ((n-coin)*10+coin)
    
    combinations = 0
    if coin <= n:
        if first_tmp not in mem:
            mem[first_tmp] = change_memo(n-coin,lst,mem)
        combinations += mem[first_tmp]
    next_coin = lst[1]
    second_tmp =(n*10+next_coin) 
    if second_tmp not in mem:
        mem[second_tmp] = change_memo(n, lst[1:],mem) 
    return combinations + mem[second_tmp]


t = time.perf_counter()
result_memo = change_memo(4, [1,2,5,7])
print(time.perf_counter() - t)
print(result_memo)