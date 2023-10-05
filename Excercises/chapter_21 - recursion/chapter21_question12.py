# pseudo code:
# def calculate catalan:
#     if c <= 1 
#     return 1
# calculate all possabilty that are valid for c-1
# for 2 - 0*1 + 1*0
# for 3 - 0*2 + 1*1  + 2*0


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
        

main_c = int(input('Enter n : '))
print(catalan(main_c))
