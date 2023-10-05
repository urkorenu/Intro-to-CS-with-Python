# print the highest value out of a dictionary
d = {'a' : 1, 'b': 2, 'c':14,'d':4, 'e':7, 'f':12}
highest_number = 0
# for i in d:
#     if d[i] > highest_number:
#         highest_number = d[i]
highest_number = list(d.values())
highest_number.sort()
print(highest_number[-1])