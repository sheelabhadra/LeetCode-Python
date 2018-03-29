#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

## SOLUTION: 2 transformation process:
# Step 1: Flip about horizontal axis.
# Step 2: Flip about the diagonal. (Transpose)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Step 1: rotate about middle row
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        
        # Step 2: take transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
