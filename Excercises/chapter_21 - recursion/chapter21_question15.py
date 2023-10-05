# ////////////////////////////////////////////////////
# Missing the right order of prints
# ////////////////////////////////////////////////////

def print_substrings(s):
    if s == '':
        return 0
    print_substrings(s[:-1])
    print(s)
    print_substrings(s[1:])
   

print_substrings('abc')


def printershrinter(s: str):
    print(s)