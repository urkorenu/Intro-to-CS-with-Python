def selectionSort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


print(selectionSort([1,4,7,3,8,3,8,3,5,8,0,5,2,7,5,3,9]))
