# Create an array of 5,5 that contain 0 or 1 and put 0 where there should be black parts in chess game.

import numpy as np

a = np.zeros((5,5),dtype=int)
print(a)
a[1::2,::2] = 1
a[0::2,1::2] = 1
print(a)