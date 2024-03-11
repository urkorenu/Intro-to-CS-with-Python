# Maman 14 - 
# //////////////////////////////////////////////////////
# //////////// Question 3  /////////////////
# //////////////////////////////////////////////////////

# Task - Compare between 2 lists and check if it contains excacly the same object no matter of the order. If it mirrors then return True else return False     

# Time complexity - O(n)

# Code - 

def isPermutation(a : list, b : list) -> bool:
    '''
    Compare between 'a' and 'b' for mirroring and return bool if it mirrors.

    Args:
    - a (list) : List of ints.
    - b (list) : List of ints.

    Returns:
    (bool) : Whether if it mirrors or not.
    '''
    # Check if the lists length is the same
    if isEqual(a,b):
        # Check if the lists are empty
        if isNotEmpty(a,b):
            # If the first object of 'a' are in the 'b' list then then save it to temp, remove the first object of 'a' and the matching object in b, then call the function again recursenly
            temp = process_lists(a[0],b,0)
            if temp != None:
                b.pop(temp)
                a.pop(0)
                return isPermutation(a,b)
            
            else:
                return False
        else:
            return True 
    return False

def isEqual(a,b):
    return len(a) == len(b)

def isNotEmpty(a,b):
    return len(a) > 0 and len(b) > 0

def process_lists(subject,b,index):
    r'''
    Recursively compare the first object of 'a' and then the full list of 'b', and returns the index of the matched 'b' or None if there isn't a match.

    Args:
    - subject (int): First object of 'a'.
    - b (list): List of ints.
    - directions (list): List of directions to explore.

    Returns:
    - index\None: Index of matched object or None.
    '''
    if not b:
        return

    tested = b[0]

    if subject == tested:
        return index

    return process_lists(subject, b[1:], index+1)

print(isPermutation([3,2,4,4],[2,4,3,5]))
