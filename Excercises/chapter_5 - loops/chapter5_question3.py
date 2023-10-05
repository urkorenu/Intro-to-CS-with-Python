s = "Python With Or 100!"
letters = 0
numbers = 0
others = 0
for i in s:
    if i.isalpha():
        letters += 1
        continue
    elif i.isnumeric():
        numbers += 1
        continue
    else:
        others += 1
print(" letters = ", letters, " numbers = ", numbers, " others = ", others)