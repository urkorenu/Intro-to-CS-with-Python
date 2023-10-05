import time


def generate_dup_list(n: int) -> list[int]:
    res = []

    for i in range(n):
        for j in range(8):
            res.append(i)

    return res



def drop_duplicates():
    global lst
    tmp = {}
    for value in lst:
        if tmp.get(value) is not None:
            continue

        tmp[value] = value

    lst = list(tmp.values())

lst = generate_dup_list(3)
print(lst)



