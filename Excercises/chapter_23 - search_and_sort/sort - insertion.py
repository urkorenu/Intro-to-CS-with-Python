def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1]= key
    return lst


print(insertionSort([1,4,7,3,8,3,8,3,5,8,0,5,2,7,5,3,9]))