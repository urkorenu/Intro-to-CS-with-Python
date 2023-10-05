def sum(num : int) -> int:
    new_num = num % 10
    if num == 0:
        return 0
    return new_num + sum(num // 10)

print(sum(1423))
