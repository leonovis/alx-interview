#!/usr/bin/python3
""" Module for rotating a matrix"""

def rotate_2d_matrix(matrix):


    n = len(matrix)

    for a in range(0, int(n / 2)):
	# row=a
        for b in range(a, n - a - 1):
            # print((a,b))
		#col=b
            temp = matrix[a][b]

            # print((a,b), (n - 1 - b,a))
            matrix[a][b] = matrix[n - 1 - b][a]

            # print((n - 1 - b,a), (n - 1 - a,n - 1 - b))
            matrix[n - 1 - b][a] = matrix[n - 1 - a][n - 1 - b]

            # print((n - 1 - a,n - 1 - b), (b,n - 1 - a))
            matrix[n - 1 - a][n - 1 - b] = matrix[b][n - 1 - a]

            # print((b,n - 1 - a))
            matrix[b][n - 1 - a] = temp 
