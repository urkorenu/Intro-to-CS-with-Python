# Create an array of 5,5 that contain 0 to 4.

import numpy as np

a = np.arange(5)
a = np.tile(a,(5,1))
print(a)
