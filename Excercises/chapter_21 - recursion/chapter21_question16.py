# ////////////////////////////////////////////////////
# Missing less recursion calls on line 28
# ////////////////////////////////////////////////////




import random
from collections import namedtuple

Point = namedtuple('Point', 'x y')

def can_go_right(dimensions: int, maze: dict[Point: int], coords: Point) -> bool:
    return (coords.y + 1 < dimensions and maze[coords.x, coords.y + 1] == 1)

def can_go_down(dimensions: int, maze: dict[Point: int], coords: Point) -> bool:
    return (coords.x + 1 < dimensions and maze[coords.x + 1, coords.y] == 1)

def maze_solved(dimensions: int, maze: dict, coords: Point) -> bool:
    return (coords.x == dimensions - 1 and coords.y == dimensions - 1 and maze[coords.x, coords.y] == 1)

def solve_maze(dimensions: int, maze: dict[Point: int], coords: Point = Point(0, 0)) -> bool:
    solved = maze_solved(dimensions, maze, coords)

    if (not solved and can_go_right(dimensions, maze,  coords)):
        solved = solve_maze(dimensions, maze, Point(coords.x, coords.y + 1))

    if (not solved and can_go_down(dimensions, maze,  coords)):
        solved = solve_maze(dimensions, maze, Point(coords.x + 1, coords.y))

    return solved


def escape(maze : dict, i : int, j: int) -> bool:
    global result
    
    if i > max_lines or j > max_lines:
        print('Wrong line')
        return 0
    
    current_location = maze[i,j]

    if current_location == 1:
        if i == max_lines and j == max_lines:
            print(f'Success')
            print(f'current location:{i},{j}')
            result = True
            return 1
        else:
            print('next move')
            print(f'current location:{i},{j}')
            escape(maze,i,j+1)
            escape(maze,i+1,j)
            return 0
    else:
        print(f'No more moves')
        return 0

# Sagi matrix generator :)
def generate_matrix(n: int) -> dict[Point: int]:
    res = {}
    for i in range(n):
        for j in range(n):
            if (j > 0 and i > 0 and res[i, j-1] == 0 and res[i-1, j] == 0):
                choice = random.randrange(1, 2)
                if (choice == 1):
                    res[i, j - 1] = 1
                else:
                    res[i - 1, j] = 1

            if ((i == n-1 and j == n-1) or (i == 0 and j == 0)):
                res[i, j] = 1
            else:
                res[(i, j)] = random.randrange(0, 2)
    return res

def print_matrix(matrix, n):
    for i in range(n):
        print('|  ', end='')
        for j in range(n):
            print(f'{matrix[i, j]}  ', end= '')
        
        print('|')

result      = False
dimensions = int(input('enter num dimensions: '))
main_matrix = generate_matrix(dimensions)
print_matrix(main_matrix, dimensions)
solved = solve_maze(dimensions, main_matrix, Point(0, 0))

print(f"result: {solved}")
exit()

max_lines   = dimensions - 1

print(main_matrix)
escape(main_matrix,0,0)
print(result)