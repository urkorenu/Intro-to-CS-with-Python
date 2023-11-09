def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        changed = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changed = 1
        if changed == 0:
            return arr
    return arr


print(bubbleSort([1,4,7,3,8,3,8,3,5,8,0,5,2,7,5,3,9]))