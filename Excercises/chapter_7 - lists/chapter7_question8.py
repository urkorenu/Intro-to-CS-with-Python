# verfying 2 lists and making new list of common values
lst1 = [15, 9, 10, 56, 23]
lst2 = [9, 4, 5, 36, 47, 10]
lst3 = [i for i in lst1 if i in lst2]
print(lst3)
# new_list = []
# for i in lst1:
#     if i in lst2:
#         new_list.append(i) 
# print(new_list)