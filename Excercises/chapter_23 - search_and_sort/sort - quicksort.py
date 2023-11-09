import random

def quickSort(lst):
    if len(lst) <= 1:
           return lst
    else:
          pivot = random.choice(lst)
          smaller = [elem for elem in lst if elem < pivot]
          equal = [elem for elem in lst if elem == pivot]
          greater = [elem for elem in lst if elem > pivot]
          return quickSort(smaller) + equal + quickSort(greater)
    

print(quickSort([1,4,7,3,8,3,8,3,5,8,0,5,2,7,5,3,9]))
