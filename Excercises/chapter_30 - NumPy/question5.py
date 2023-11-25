# Create an array of 8,8 that contain 0 or 1 and put 0 where there should be black parts in chess game.

import numpy as np

a = np.arange(2)
b = np.where(a == 0,1,0)
a = np.tile(np.vstack((a,b)),(4,4))
print(a)
