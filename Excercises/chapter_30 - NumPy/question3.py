# Create an array of 4,4 that contain number between -5-5 and print how many elements are smaller then 0.

import numpy as np

a = np.random.randint(-5,6,(4,4))
print(a)
print(np.sum(a<0))