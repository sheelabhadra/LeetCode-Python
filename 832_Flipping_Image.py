# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] 
# horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, 
# inverting [0, 1, 1] results in [1, 0, 0].

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(A), len(A[0])
        
        for i in range(M):
            for j in range(N//2):
                A[i][j],  A[i][N-1-j] = A[i][N-1-j], A[i][j]
        
        for i in range(M):
            for j in range(N):
                A[i][j] = 1 - A[i][j]
        
        return A
