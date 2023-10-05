# merge of 2 dictioneries
dict_union  = ({'a' : 1, 'b': [1,2], 'c':3},{'b':4, 'a':[5,6,7], 'e':8})
result      = {}
for d in dict_union:
    for key in d:
        if key not in result:
            result[key] = d[key]
        else:
            result[key] = [result[key], [d[key]]]
print(result)
