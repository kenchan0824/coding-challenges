Matrix Chain Multiplication
===



Given a chain of matrices such that any matrix may be multiplied by the previous matrix, find the cost of the best association such that the result is obtained with the minimum number of arithmetic operations.

For a chain of `n` matrices `M[1], M[2], ..., M[n]`, their dimensions are defined as `(A[0], A[1]), (A[1], A[2]), ..., (A[n-1], A[n])`. The cost of multiplying two matrics with dimensions `(A[i-1], A[i])` and `(A[i], A[i+1])` is `A[i-1] x A[i] x A[i+1]`.



#dynamic-programming 	#O(n^3)