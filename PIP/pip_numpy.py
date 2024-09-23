import numpy as np

vector_a = np.array([1, 2, 3, 4, 5])
print(vector_a**2)
print("\n")

matrix_b = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix_b**2)
print("\n")

zeros_c = np.zeros((3, 3))
print(zeros_c)
print("\n")

ones_d = np.ones((3, 3))
print(ones_d)
print("\n")

jumlah_matrix = matrix_b + matrix_b**2 + matrix_b*2 + ones_d
print(jumlah_matrix)