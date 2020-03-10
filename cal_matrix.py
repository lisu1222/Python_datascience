'''
multiply a matrix by a scalar, caculates means row- and column-wise, creates 
a numpy matrix from numpy arrays, and display it by row and element
'''

import numpy as np 

def mult_scalar(m, s):
	'''multiply a mtrix m by scalar s'''
	matrix = np.empty(m.shape)
	m_shape = m.shape
	for i in range(m_shape[0]):
		matrix[i] = np.array([x * s for x in m[i]])
	return matrix

def display(m):
	cols = m.shape[1]
	for i, row in enumerate(m):
		print ('row', str(i) +':', row, 'elements: ', end = ' ')
		for col in range(cols):
			print (row[col], end = ' ')
		print ()

if __name__ == "__main__":
	v1, v2, v3 = [1, 7, -4], [2, -3, 10], [3, 5, 6]
	A = np.matrix([v1,v2,v3])
	print ( 'matrix A:\n', A)
	scalar = 0.5
	B = mult_scalar(A, scalar)
	print ('\nmatrix B:\n', B)
	mu_col = np.mean(A, axis = 0, dtype = np.float64)
	print ('\nmean A (column-wise):\n', mu_col)
	mu_row = np.mean(A, axis = 1, dtype = np.float64)
	print ('\nmean A (row-wise):\n', mu_row)
	print ('\nmatrix C:')
	C = np.array([[2,14,-8],[4,-6,20],[6, 10, 12]])
	print (C)
	print('\ndisplay each row and elements:')
	display(C)



