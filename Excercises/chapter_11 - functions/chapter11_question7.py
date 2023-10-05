import time

# returns the highest int of a list
def find_max_grade(grades):
    max = 0
    for grade in grades:
        if grade > max:
            max = grade
    return max

def find_max_grade_sagi(grades: list[int]) -> int:
    # max = 0

    # for grade in grades:
    #     if max >= grade:
    #         continue
    #     max = grade

    # return max
    max = 0
    for grade in grades:
        if grade > max:
            max = grade
    return max

def generate_number_list(n: int) -> list[int]:
    res = []

    for i in range(n):
        res.append(i+1)

    return res

def main():
    grades = generate_number_list(10000000)
    sagi_time = time.perf_counter_ns()
    max = find_max_grade_sagi(grades)
    sagi_time = time.perf_counter_ns() - sagi_time
    koren_time = time.perf_counter_ns()
    max = find_max_grade(grades)
    koren_time = time.perf_counter_ns() - koren_time
    
    print(max)
    print(f'sagi_time = {sagi_time}')
    print(f'koren_time = {koren_time}')

    if (sagi_time < koren_time):
        print('sagi')
    else:
        print('koren')
    
main()
