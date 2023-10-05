# ////////////////////////////////////////////////////
# Missing less recursion calls on line 28
# ////////////////////////////////////////////////////




import random

def escape(maze : dict, i : int, j: int) -> bool:
    global result
    
    if i > max_lines or j > max_lines:
        # print('Wrong line')
        return 0
    
    current_location = maze[i,j]

    if current_location == 1:
        if i == max_lines and j == max_lines:
            # print(f'Success')
            # print(f'current location:{i},{j}')
            result = True
            return 1
        else:
            # print('next move')
            # print(f'current location:{i},{j}')
            escape(maze,i,j+1)
            escape(maze,i+1,j)
            return 0
    else:
        # print(f'No more moves')
        return 0

# Sagi matrix generator :)
def generate_matrix(n: int) -> dict[tuple[int, int]: int]:
    res = {}
    for i in range(n):
        for j in range(n):
            res[(i, j)] = random.randrange(0, 2)
    return res

result      = False
n_matrix    = 4
main_matrix = generate_matrix(n_matrix)
max_lines   = n_matrix - 1

print(main_matrix)
escape(main_matrix,0,0)
print(result)