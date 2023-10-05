def reverse_str(s : str) -> str:
    if s == s[0]:
        return s[0]
    return s[-1] + reverse_str(s[:-1])
    res = s[-1]
    s = s[:-1]
    return res + reverse_str(s)

print(reverse_str('sagi'))