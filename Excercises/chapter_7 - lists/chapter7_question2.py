# Finding avg lengh of strings and printing string that above the avg length
lst = ['Python', 'With', 'Or', 'Koren']
avg_len = sum([len(x) / len(lst)  for x in lst])
new_lst = [x for x in lst if len(x) > avg_len]
print(new_lst)
# sum = 0
# for i in list:
#     sum += len(i)
# sum = sum / len(list)
# print("The avarage length: ", sum)
# for j in list:
#     if len(j) > sum:
#         new_list.append(j)
# print(new_list)

