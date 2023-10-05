# creates keys of n number of letters in string and tracks how many it appears in a string
str     = 'AASCBAAS'
n       = 1
result  = {}
index   = 0

for i in str:
    extracted_str = str[index:n+index]
    if len(extracted_str) < n:
        break
    elif extracted_str not in result:
        result[extracted_str] = 1
    else:
        result[extracted_str] += 1
    index += 1
    
print(result)
