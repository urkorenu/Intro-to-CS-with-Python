def change(n : int, lst : list) -> int:
    if n == 0:
        return 1
    if lst == []:
        return 0
    coin = lst[0]
    combinations = 0
    if coin <= n:
        combinations += change(n-coin, lst)
    return combinations + change(n, lst[1:])


result = change(4, [1,2,5,7])
print(result)
