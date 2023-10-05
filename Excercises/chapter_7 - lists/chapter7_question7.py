# calculate the sum of index i in a list
lst =[1, 2, 3, 4]
new_list = [lst[0]]
pre_index = 0
for i in range(1,len(lst)):
    new_list.append(lst[i]+new_list[pre_index])
    pre_index += 1

print(new_list)