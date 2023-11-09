# ////////////////////////////////////////////////////
# Missing the right order of prints
# ////////////////////////////////////////////////////

def print_substrings(s):
    if s == '':
        return 0
    print_substrings(s[:-1])
    print(s)
    print_substrings(s[1:])
   

# def printershrinter(s: str):
#     if (s == ''):
#         return s

#     print(s + printershrinter(s[:-1]))
#     return s

# def shrinterprinter(s: str):
#     if (len(s) == 1):
#         return s
    
#     print(shrinterprinter(s[1:]))
#     return s

# s = 'abc'
# printershrinter(s)

