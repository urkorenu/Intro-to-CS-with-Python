# Create an array of 10,10 that contains number betweer 0-1 and print the min and max of the array

import numpy as np

a = np.random.random((10,10))
print(a.min())
print(a.max())