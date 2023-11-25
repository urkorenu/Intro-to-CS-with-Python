# Create a random array and print it in some conditions

import numpy as np

a = np.random.randint(0,99,(10,10))
mask_3 = a % 3 != 0
mask_5 = a % 3 != 0 and a % 5 != 0
mask_6 = a % 2 == 0 and a % 6 == 0
print(a)

