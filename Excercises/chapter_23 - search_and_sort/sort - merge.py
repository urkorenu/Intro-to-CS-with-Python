def merge(left,right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+= 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    mid = len(sequence) // 2
    left_sequence = merge_sort(sequence[:mid])
    right_sequence = merge_sort(sequence[mid:])
    return merge(left_sequence, right_sequence)


print(merge_sort([1,4,7,3,8,3,8,3,5,8,0,5,2,7,5,3,9]))