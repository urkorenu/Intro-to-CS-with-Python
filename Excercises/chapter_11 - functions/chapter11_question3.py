# calculate avg of each list and return the smaller one
def min_avg_list(a, b):
    avg_a = sum(a)/len(a)
    avg_b = sum(b)/len(a)
    return min(avg_a, avg_b)
    # avg_a = 0
    # avg_b = 0
    # for i in a:
    #     avg_a += i/len(a)
    # for i in b:
    #     avg_b += i/len(b)
    # if avg_a < avg_b:
    #     return avg_a
    # else:
    #     return avg_b
print(min_avg_list([1,2,3], [4,6,8]))

    
    
