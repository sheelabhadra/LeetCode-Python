First Cycle (Involves Red Elements)
 1  2  3 4 
 5  6  7  8 
 9 10 11 12 
 13 14 15 16 

 
Moving first group of four elements (First
elements of 1st row, last row, 1st column 
and last column) of first cycle in counter
clockwise. 
 4  2  3 16
 5  6  7 8 
 9 10 11 12 
 1 14  15 13 
 
#Moving next group of four elements of 
first cycle in counter clockwise 
 4  8  3 16 
 5  6  7  15  
 2  10 11 12 
 1  14  9 13 

Moving final group of four elements of 
first cycle in counter clockwise 
 4  8 12 16 
 3  6  7 15 
 2 10 11 14 
 1  5  9 13 


Second Cycle (Involves Blue Elements)
 4  8 12 16 
 3  6 7  15 
 2  10 11 14 
 1  5  9 13 

Fixing second cycle
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-1-i):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i] # left to top
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j] # bottom to left
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i] # right to bottom
                matrix[j][n-1-i]=tmp # top to right
                
