# Returns all possabily dice results in dict
results = {}
for i in range(1,7):
    for j in range(1,7):
        if i+j not in results:
            results[i+j] = []
        results[i+j].append((i, j))
print(results)