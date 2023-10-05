#  * a number of his index and sum of * of following indexes
lst = ['3', '2', '5', '1']
sum = 0
sum_2 = 0
for i in range(len(lst)):
    sum += i*int(lst[i])
    if i == len(lst) - 1:
        break
    sum_2 += int(lst[i])*int(lst[int(i)+1])
print(sum)
print(sum_2)


