def fast_power(a : int,b : int) -> int:
    if b == 0:
        return 1
    elif b % 2 == 0:
        return a * fast_power(a, b - 2) * a
    return a * (fast_power(a, b - 1))

print(fast_power(8,3))