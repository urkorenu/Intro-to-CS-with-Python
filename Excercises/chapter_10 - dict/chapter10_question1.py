# Checks if a string contians all alphabetic letters
str = "The five boxing wizards jump quickly" 
d = {}
for char in str:
    if char.isalpha():
        d[char.lower()] = True
if len(d) == 26:
    print(True)
else:
    print(False)
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new_letters = []
# for i in str:
#     i = i.lower()
#     if i in new_letters:
#         continue
#     elif i.isalpha():
#         new_letters.append(i)
# new_letters.sort()
# if letters == new_letters:
#     print(True)
# else:
#     print(False)
