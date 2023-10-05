# Turning nested lists into set
lst = [[1, 2, 2, 4, 3, 6],
       [5, 1, 3, 4],
       [9, 5, 7 ,1],
       [2, 4, 1, 3]]
result = set(lst[0])
for l in lst[1:]:
    result.update(l)
result = list(result)
print(result)
# x = set()
# for i in lst:
#     for j in range(len(i)):
#         x.add(i[j])
# print(x)