import time

def drop_duplicates(lst):
    new_lst = []
    for value in lst:
        if value not in new_lst:
            new_lst.append(value)
    return new_lst

def generate_dup_list(n: int) -> list[int]:
    res = []

    for i in range(n):
        for j in range(8):
            res.append(i)

    return res

def get_none_dup_list(values: list[int]) -> list[int]:
    tmp = {}
    res = []
    
    for value in values:
        if tmp.get(value) != None:
            continue
        
        tmp[value] = value
        res.append(value)

lst = generate_dup_list(100)
koren_perf  = time.perf_counter_ns()
koren_res   = drop_duplicates(lst)
koren_perf  = time.perf_counter_ns() - koren_perf
sagi_perf   = time.perf_counter_ns()
sagi_res    = get_none_dup_list(lst)
sagi_perf   = time.perf_counter_ns() - sagi_perf
print(f'sagi_res: {sagi_res}, koren_res: {koren_res}')
print(f'sagi_perf: {sagi_perf}, koren_perf: {koren_perf}')


