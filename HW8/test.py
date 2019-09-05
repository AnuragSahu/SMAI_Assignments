import numpy as np

a = np.array([[-0.36,-0.330],[-0.33,-2.70]])

b = np.array([[ 0.99250756, -0.12218326 ]]).T

#[-0.12218326,  0.99250756]
print(a.dot(b))