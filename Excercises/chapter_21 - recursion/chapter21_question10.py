def is_palindrome(s : str) -> str:
    # if s == '':
    #     return True
    # elif s == s[0]:
    #     return True
    # elif s[0] == s[-1]:
    #     return is_palindrome(s[1:-1])
    # else:
    #     return False
    if len(s) < 2:
        return True
    return s[-1] == s[0] and is_palindrome(s[1:-1])
    


print(is_palindrome(''))
print(is_palindrome('o'))
print(is_palindrome('or'))
print(is_palindrome('oro'))
print(is_palindrome('oror'))
print(is_palindrome('ororo'))