def binarySearch(lst, x):
    low = 0
    mid = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low) //2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print(binarySearch([0, 1, 2, 3, 4, 5, 7, 8, 9], 3))