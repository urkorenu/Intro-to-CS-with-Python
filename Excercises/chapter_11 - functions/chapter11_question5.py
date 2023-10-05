# calculate a list muptiply by next even number, if there is no even number then return 1
def mult_even_nums(n):
    res = 1
    while n > 0 :
        num = n % 10
        if num % 2 == 0:
            res = res * num
        n //= 10
    return res
print(mult_even_nums(32489237))



    
    
