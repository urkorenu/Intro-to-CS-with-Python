
# ///////////// Question 1 ///////////////


def what(m :list) -> bool:
    n = len(m)
    for x in range(n):
        for y in range(n - 1):
            if m[x][y] > m[x][y + 1]:
                return False
    for x in range(n):
        for y in range(n - 1):
            if m[y][x] > m[y + 1][x]:
                return False
    return True

def riddle(m : list, val) -> bool:
    n = len(m)
    for x in range(n):
        for y in range(n):
            if m[x][y] == val:
                return True
    return False

def test(m : list) -> bool:
    n = len(m)
    for r in range(n - 1):
        for c in range(n):
            for i in range(n):
                if m[r][c] > m[r + 1][i]:
                    return False
    return True

# ///////////// Part 1 ///////////////
# O(n)

def createSetFromList(m : list) -> set:
    value_set = set()
    for sublist in m:
        value_set.update(sublist)
    return value_set

def findValWhat(m : list, val: str) -> bool:
    value_set = createSetFromList(m)
    return val in value_set

# ///////////// Part 2 ///////////////
# 
# ///////////// Missing ///////////////

# ///////////// Commands ///////////////

# a = [['a','b'],['c','d']]
# print(f'What: {what(a)}')
# print(f'Test: {test(a)}')
# print(f'Find Val: {findValWhat(a,"d")}')


# ///////////// Question 2 ///////////////
def strictlyIncreasing(m : list):
    result_list = []
    n = len(m)
    for x in range(1,n):
        if m[x] != m[x-1]:
            print(f'res list: {result_list}')
            print(f'm[x] : {m[x]}')
            if result_list != []:
                if check_lists(m,result_list, x):
                    result_list.append([result_list[-1],m[x]])
            if m[x-1] < m[x]:
                print('normal add')
                result_list.append([m[x-1],m[x]])


            
    if result_list == []:
        result_list.append(0)
    return result_list
        
def check_lists(m, list, cur_pos):
    if list != []:
        len_last_list = len(list[-1])
        if m[cur_pos-len_last_list] == list[-1][0]:
            return True
    return False
    
    
# if m[0] < m[1]:
# add list of [m0,m1]
# go then to next number
# if m[1] < m[2]:
# add list
# check if it can follow the previous list
a = [1,2,4,4,5]
b = [1,3,2]
c = [5,4,3,2,1]
print(f'A = {strictlyIncreasing(a)}')
print(f'B = {strictlyIncreasing(b)}')
print(f'C = {strictlyIncreasing(c)}')