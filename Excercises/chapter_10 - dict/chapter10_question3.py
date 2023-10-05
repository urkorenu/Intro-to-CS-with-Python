# Calculate how many times a number apears in n, return the most apeared numbers, if there is more then 1 - it returns the min number
n = 111222334
calculated = {}
max_used = 0
result = []
for i in str(n):
    if i not in calculated:
        calculated[i] = []
    calculated[i].append((i))
for i in calculated:
        if len(calculated[i]) > max_used:
            max_used = len(calculated[i])
for i in calculated:
     if len(calculated[i]) == max_used:
          result.append(int(i))
print(min(result))