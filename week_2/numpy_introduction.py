import numpy as np

v = np.ones((5,1))
print(v)

v[2, 0] = 3.14
print(v)

v_row = v.copy().T
print(v_row)

x = np.dot(v, v_row)
print(x)

v_rand = np.random.rand(10,1)
print(v_rand)

A = np.random.normal(10, 2, (2,5))
print(A)

col2 = A[:,1]
print(col2)

cols34 = A[:,2:4]
print(cols34)

B = np.random.rand(5,2)
result_mat = np.dot(A, B)
print(result_mat)