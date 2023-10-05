def find_maximum(lst : list) -> int:
    num = 0
    if isinstance(lst, int):
        return lst
    elif lst == []:
        return -1
    else: 
        for i in lst:
            if i > num:
                num = find_maximum(i)
    return num

print(find_maximum(1))
print(find_maximum([9,3,2,10,4]))
print(find_maximum([]))
