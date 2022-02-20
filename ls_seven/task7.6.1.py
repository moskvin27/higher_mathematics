import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
print("Решение системы:")
print(np.linalg.solve(A, B))
# print (A[0][0], A[1][0], A[2][0])