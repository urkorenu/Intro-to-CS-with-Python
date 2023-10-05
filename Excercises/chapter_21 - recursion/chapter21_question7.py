def sum_nested_list(lst : list) -> int:
    num = 0
    if isinstance(lst, int):
        return lst
    for i in lst:
        num += sum_nested_list(i)
    return num

# print(sum_nested_list(1))
# print(sum_nested_list([1]))
# print(sum_nested_list([1,2]))
# print(sum_nested_list([[1,2]]))
print(sum_nested_list([1,2,3,[1,[1,2,[1,2,3,[1,2,3]]]]]))