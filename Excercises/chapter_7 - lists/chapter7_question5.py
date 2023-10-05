# Fidning string in list and arrange it by lexographic order
lst = ['Python with or', 'Or blapython or', 'Python -- koren', 'Pythonwithor']
new_lst = []
for i in lst:
    new_i = i.split()
    for j in new_i:        
        j = j.lower()
        if 'python' == j:
            new_lst.append(i)
new_lst.sort(reverse=True)
print(new_lst)