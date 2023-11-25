# Maman 14 - 

# //////////// Question 1 //////////////////

# Task - Write a function that takes an array and return the biggest gap between 2 ints. The bigger number must be before the lowest number

#  This function utilizes recursion to identify the largest difference between two numbers in an array.
#  It begins by selecting a reference number (the 'subject') and compares it with all subsequent numbers in the array,
#  determining the maximum gap between them. The function repeats this process with each subsequent number as the 'subject' until it reaches the second-to-last element of the array.
#  Ultimately, it returns the largest gap found among these comparisons."

#  Time complexity - O(n): processes each element while testing it only once.

def maximal_drop(array, start_index = 0, max_gap = 0):
    """
    Finds the largest gap between two numbers in an array where the larger number appears before the smaller one.

    Args:
    - array (list): The input list of integers.
    - start_index (int): The index of the current 'subject' number being compared.
    - max_gap (int): The maximum gap found so far (initially set to 0). 

    Returns:
    - int: The largest gap between two numbers where the larger number precedes the smaller one.
    """

# If reached the end of the list, return the max_gap
    if start_index == len(array) - 1:
        return max_gap

# Loop that iterates through the array once for each element, 
# Calculating the gap between the current element and all subsequent elements. 
# It updates the max_gap variable if a larger gap is found, 
    for i in range(start_index + 1, len(array)):
        gap = array[start_index] - array[i]
        if gap > max_gap:
            max_gap = gap

# Recursively call the function with the updated index          
    return maximal_drop(array, start_index + 1, max_gap)

# Test the function
# print(f'max drop: {maximal_drop([5, 21, 3, 22, 12, 7, 27, 6, 4])}')




# //////////// Question 2 //////////////////

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
# array = create_2d_array(5)
# print(array)
# # Test the function
# print(isSink(array,5))


# //////////// Question 3  /////////////////
# 
# Task -            Write a function that takes 2d array and x,y and checks if there is combination  of at least 2 object that are 
#                   touching each other. That function returns the number of touching objects, if there is no combination
#                   (at least 2) then the function return 0

# Plan -            Checks the x,y given as arg and checking if it = 1, if it does then check all the directions (8) recursively
#                   and add +1 to counter. At the end it return all of the surrounding objects.

# Time complexity - 

# Code - 

class ex14():
    def __init__(self):
        self.array = create_2d_array(5)
        self.sum = 0
        self.checked_objects = []
        self.len = len(self.array) - 1
        print(self.array)

    def size(self,x : int,y : int) -> int:
        '''
        Calculate the size of the combination (at least 2 touching objects).

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - sum (int): Sum of combinations.
        '''
        if self.is_inrange(x,y):
            return
        if self.is_zero(x,y):
            return
        if (x,y) not in self.checked_objects:
            self.checked_objects.append((x,y))
            self.sum += 1
        # right
        if self.check_dir(x+1,y):
            print('right')
            self.sum += 1
        # top right
        if self.check_dir(x+1,y+1):
            self.sum += 1
        # top
        if self.check_dir(x,y+1):
            self.sum += 1
        # top left
        if self.check_dir(x-1,y+1):
            self.sum += 1
        # left
        if self.check_dir(x-1,y):
            self.sum += 1
        # bottom left
        if self.check_dir(x-1,y-1):
            self.sum += 1
        # bottom
        if self.check_dir(x,y-1):
            self.sum += 1
        # bottom right 
        if self.check_dir(x+1,y-1):
            self.sum += 1
        return self.sum

    def check_dir(self,x,y):
        '''
        Checks given x,y (new direction) that it is range of the array, that the object is 1 and not in the checked_objects list. If it pass the conditions- 
        Appending the new object cords to the checked_object list, call the size function again with the new cords adn return True.
        
        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool).
        '''
        if self.is_inrange(x,y):
            return
        if self.array[x][y] == 1 and (x,y) not in self.checked_objects:
            self.checked_objects.append((x,y))
            self.size(x,y)
            return True
        return False
    
    def is_inrange(self,x,y):
        '''
        Checks given x,y that it is range of the array.

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool).
        '''
        if not (0 <= x <= self.len) or not (0 <= y <= self.len):
            return True
        else:
            return False
        
    def is_zero(self,x,y):
        '''
        Checks if the given object is zero.

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool).
        '''
        if self.array[x][y] == 0:
            return True
        else:
            return False


a = ex14()
print(a.size(4,3))

