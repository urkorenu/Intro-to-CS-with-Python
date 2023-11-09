def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i 
    return -1

print(search([0, 1, 2, 3, 4, 5, 7, 8, 9], 7))