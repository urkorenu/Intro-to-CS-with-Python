# Merging two lists, verify for duplicates, sort by upscale
list_union =[[1, 2, 3, 1], [2, 3, 4, 2]]
new_list = []
for i in range(len(list_union)):
    for j in list_union[i]:
        if j in new_list:
            continue
        else:
            new_list.append(j)
new_list.sort()
print(new_list)