import numpy as np

def even_numbers(twoDarray : np) -> int:
    count = 0
    if twoDarray.ndim != 2:
        return None 
    for row in twoDarray:
        for elem in row:
            if elem % 2 == 0: 
                count += 1
    return count

# print(even_numbers(np.array([[1,2],[6,4]])))

def avarage(twoDarray : np):
    count = 0
    avarage = 0
    if twoDarray.ndim != 2:
        return None
    for row in twoDarray:
        for elem in row:
            count += 1
            avarage += elem
    avarage = avarage / count
    return avarage

# print(avarage(np.array([[1,2],[3,4]])))

def get_corner_avarage(twoDarray : np):
    if twoDarray.ndim != 2:
        return None
    avarage = 0
    count = 0
    for row in twoDarray:
        avarage += (row[0] + row[-1])
        count += 2
    avarage = avarage / count
    return avarage

# print(get_corner_avarage(np.array([[1,2,3],[3,4,5]])))


# ////// Functions of creating  arrays //////////

#  Takes array dimentions and return array full of ones
# np.ones((dimentions:tuple))

#  Takes array dimentions and return array full of zeros
# np.zeros((demintions:tuple))

#  Takes array dimentions and return array full of object
# np.full(dimentions:tuple,object)

#  Takes int and return cubic two dimentional array that is full of 0 except the אלכסון that is 1
# np.eye(int)

#  Same as eye function but takes vector as input and return same as eye function but instead of 1 it fills the vector
# np.diag(vector)

#  Takes dimentions and return empty array
# np.empty(array)

# Take dimentions and return array with random values between 0-1
# np.random.random(dimention)

# Takes range of int and dimention and return array of random ints between the range
# np.random.randint(min val, max val, dimention)

# Method that operates on array and return index that different from 0
# np = array
# np.nonzero()
# To extract them you can use this:
# np[np.nonzero()]

# Function that takes : start, stop, finish and returns array with those parameters
# a = np.arrange(2,8)
# a = [2 3 4 5 6 7] 

# Function that takes : start stop and num and return array of that is divided by num
# np.linspace(start,finish,num)
# a = np.linspace(0,10,5)


# ////////// Functions of arrays //////////////

# len - reutrn length of dimentions
# min - return minimum int of array
# max - return maximum int of array
# argmin = return the index of minimum int of array
# argmax = return the index of maximum int of array
# mean - return the avarage of array
# sum - return the sum of array, option for x.sum(axis = 0) that will sum by colum (axis = 1 is row)
# all - return True if all the value of array is different from 0, else return False
# any - return True if there is a value that is different from 0, else return False
# sort - update array to sorted one by axis (1 = row, 0 = colum)
# where(array == val) - return indexs that the val is there


# ////////// Function on arrays //////////////
# Operates on every element of array

# a = array
# a + 2 = every element + 2, Same goes for +-/*

# a + b = merge of elemnts, Same goes for +-/*

# np.dot(a,b) = sum of 2 elements multiple by elemnts of 2 array

# np.where(condition, True value, False value) = change array, change by the contion and the true\false inputs


# ///////// Bool on arrays //////////////
#  bool operator will operate on every element

#  np > 3 = return bool array of every element compared to 3. 4 will be placed with True. 

#  np[np>3] = return the elements that are True


# //////// Chnaging dimentions of arrays ///////////

# a.reshape(dimentions) = Takes dimention and change the array to the new dimentions, The new dinetions must contains the same num of elements as the old dimentions.

# a.vstack((a,b)) = Takes tuple of arrays and return the arrays in vertical shape. Doesnt change the arrays but creatingg new array.

# a.hstack((a,b)) = Takes tuple of arrays and return the arrays in horizontal shape. Doesnt change the arrays but creatingg new array.

