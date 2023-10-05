# check if a string is palindrome
def is_palindrome(n):
    new_n = n[::-1]
    if n == new_n : 
        return True
    else:
        return False
print(is_palindrome('abba'))



    
    
