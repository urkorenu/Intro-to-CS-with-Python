# sum of 2 matrix 
import random   
def generate_matrix(n: int) -> dict[tuple[int, int]: int]:
    res = {}
    for i in range(n):
        for j in range(n):
            res[(i, j)] = random.randrange(0, 10)

    return res

matrix_main = generate_matrix(4)
matrix_2    = generate_matrix(4)

for i in matrix_main:
    matrix_main[i] += matrix_2[i]

print(matrix_main)