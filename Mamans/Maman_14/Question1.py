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
print(f'max drop: {maximal_drop([5, 21, 3, 22, 12, 7, 27, 6, 4])}')

