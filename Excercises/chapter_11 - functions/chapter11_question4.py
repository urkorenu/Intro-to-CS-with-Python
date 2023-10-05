# calculate a list muptiply by x of all number that divided by x without remenents, if there is no one that divided by x with without rememnent then return 1
def mul_nums(lst, x):
    res = 1
    for num in lst:
        if num % x == 0:
            res = res * num
    return res
print(mul_nums([3,4,2,5,6,9], 2))



    
    
