# Maman 14 - 
# //////////////////////////////////////////////////////
# //////////// Question 1 //////////////////
# //////////////////////////////////////////////////////

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
# array = create_2d_array(5)
# print(array)
# # Test the function
# print(isSink(array,5))

# //////////////////////////////////////////////////////
# //////////// Question 3  /////////////////
# //////////////////////////////////////////////////////

# Task -            Write a function that takes 2d array and x,y and checks if there is combination  of at least 2 object that are 
#                   touching each other. That function returns the number of touching objects, if there is no combination
#                   (at least 2) then the function return 0

# Plan -            Checks the x,y given as arg and checking if it = 1, if it does then check all the directions (8) recursively
#                   and add +1 to counter. At the end it return all of the surrounding objects.

# Time complexity - O(n^2)

# Code - 

class ex14():
    def __init__(self):
        """
        Initializes the Ex14 Q3 class.
        - array: 2D array generated by create_2d_array.
        - combination_size: Tracks the size of the combination.
        - checked_objects: List to store checked (x, y) positions.
        - array_size: Size of the array.
        """
        self.array              = create_2d_array(5)
        self.combination_sum    = 0
        self.checked_objects    = []
        self.array_size         = len(self.array) - 1
        print(self.array)

    def _rec_size(self, x : int, y : int) -> int:
        '''
        Calculate the size of the combination (at least 2 touching objects).

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - combination_sum (int): Sum of combinations.
        '''
        # Check if the position is out of range or is zero.
        if self.is_out_of_range(x,y) or self.is_zero(x,y):
            return
        
        # If the position is not in the list of checked objects, add it and increment combination_size
        if self.is_notincheckedobject(x,y):
            self.checked_objects.append((x,y))
            self.combination_sum += 1

        # Define directions to explore adjacent positions and return the result of processing them recursively
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        return self.process_directions(x, y, directions)

    def process_directions(self, x, y, directions):
        '''
        Recursively explores the neighboring directions and updates the combination_size.

        Args:
        - x (int): Row (x) of the array.
        - y (int): Column (y) of the array.
        - directions (list): List of directions to explore.

        Returns:
        - combination_size (int): Sum of combinations.
        '''
        if not directions:
            return

        dx, dy = directions[0]
        new_x, new_y = x + dx, y + dy
        if self.check_dir(new_x, new_y):
            self.combination_sum += 1

        return self.process_directions(x, y, directions[1:])
    
    def is_notincheckedobject(self,x,y):
        '''
        Checks given x,y that it is in the checked objects list.

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool): Whether (x, y) is not in the checked objects list.
        '''
        return (x,y) not in self.checked_objects
    
    def is_out_of_range(self,x,y):
        '''
        Checks given x,y that it is range of the array.

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool): Whether (x, y) is out of range.
        '''
        return not (0 <= x <= self.array_size) or not (0 <= y <= self.array_size)
        
    def is_zero(self,x,y):
        '''
        Checks if the given object is zero.

        Args:
        - x (int):  Row (x) of the array.
        - y (int):  Colum (y) of the array.

        Returns:
        - (bool): Whether the object at (x, y) is zero.
        '''
        return self.array[x][y] == 0

    def check_dir(self,x,y):
        '''
        Checks the new direction at (x, y) against certain conditions.
        
        Args:
        - x (int): Row (x) of the array.
        - y (int): Column (y) of the array.

        Returns:
        - (bool): Whether the conditions are met.
        '''
        if self.is_out_of_range(x,y):
            return False
        if self.array[x][y] == 1 and self.is_notincheckedobject(x,y):
            self.checked_objects.append((x,y))
            self._rec_size(x,y)
            return True
        return False
    
    def size(self,x,y):
        '''
        Call the main size recursive function, check and update the combination sum if it hasnt reached min combinations.

        Args:
        - x (int): Row (x) of the array.
        - y (int): Column (y) of the array.

        Returns:
        - combination_size (int): Sum of combinations.
        '''
        self._rec_size(x,y)
        if self.combination_sum < 2:
            self.combination_sum = 0
        return self.combination_sum

    
a = ex14()
print(a.size(4,3))


