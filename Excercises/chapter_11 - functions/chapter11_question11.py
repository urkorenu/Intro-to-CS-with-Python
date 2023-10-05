import random   
def generate_matrix(n: int) -> dict[tuple[int, int]: int]:
    res = {}
    for i in range(n):
        for j in range(n):
            res[(i, j)] = random.randrange(0, 10)

    return res

def mul_matrix_by_scalar(mat: dict, scalar: int) -> dict[tuple[int, int]: int]:
    global matrix_main
    for key in mat:
        mat[key] = mat[key] * scalar
    
matrix_main = generate_matrix(4)
print(matrix_main)
mul_matrix_by_scalar(matrix_main, 8)
print(matrix_main)