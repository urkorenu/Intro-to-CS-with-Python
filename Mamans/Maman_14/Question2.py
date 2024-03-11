# //////////////////////////////////////////////////////
# //////////// Question 2 //////////////////
# //////////////////////////////////////////////////////

# Task - Write a function that takes a two dimension cubic array, Checks for a sink (a row that all objects are 0 and the all the colum object are 1, except the sink location) 
# and return the y of that hole, if there isnt sink return -1.


# Time complexity: O(n^2)

import numpy as np

def create_2d_array(n):
    '''
    Generate a random 2D array of size n x n that contains 0s or 1s

    Args:
    - n (int): The size of the 2D array.

    Returns:
    - numpy.ndarray: A randomly generated 2D array.
    '''
    array = np.random.randint(0,2,(n,n))
    # To ensure there is an sink - Turn whole 2 into 0
    array[2] = 0
    return array

def isSink(array, n , row=0, colum=0):
    """
    Checks for the presence of a 'sink' in a 2D cubic array and returns its y-coordinate if found.

    A 'sink' is defined as a row that contains all 0s and all columns with 1s except at the sink location.

    Args:
    - array (numpy.ndarray): The 2D cubic array to search for a 'sink'.
    - n (int): The size of the array (n x n).
    - row (int): Starting row index for search (default: 0).
    - column (int): Starting column index for search (default: 0).

    Returns:
    - int: The y-coordinate of the 'sink' if found, else returns -1.
    """

# If reached the end of the list, return the max_gap
    if n - row == 0 or n - colum == 0:
        return -1
    
# If there isnt other object then 0
    if not np.any(array[row]):
        for i_row in range(0,n):

# Ignore the element in the selected row
            if i_row == row:
                continue

# If the checked element isnt 1 the break the loop because its not a 'sink'
            if array[i_row][colum] != 1:
                break

# If the loop continued till the last element then it returns the row
            elif n-i_row == 1:
                return row
# Checks recursely the next colum
        return isSink(array, n , row , colum + 1)
    else: 
# Checks recursely the next row
        return isSink(array, n, row+1 , colum)


# Generate a 2D array and find a sink
array = create_2d_array(5)
print(array)
# Test the function
print(isSink(array,5))