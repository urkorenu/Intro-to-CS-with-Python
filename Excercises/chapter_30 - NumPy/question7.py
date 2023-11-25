# Create a random array that replace every odd number to 1.

import numpy as np

a = np.random.randint(0,99,(4,4))
mask = a % 2 != 0
a[mask] = 1
print(a)
