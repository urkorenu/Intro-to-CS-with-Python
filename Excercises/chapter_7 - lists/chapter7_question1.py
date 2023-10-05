# Finding odd numbers in nested lists
A = [[1, 2], [3, 4], [14, 15], [44, 322]]
new_list = []
for i in A:
    for j in i:
        if j % 2 == 0:
            continue
        else:
            new_list.append(j)
print(new_list)