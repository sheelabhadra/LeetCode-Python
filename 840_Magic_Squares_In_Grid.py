#A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, 
#and both diagonals all have the same sum.

#Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

#Example 1:

#Input: [[4,3,8,4],
#        [9,5,1,9],
#       [2,7,6,2]]
#Output: 1
#Explanation: 
#The following subgrid is a 3 x 3 magic square:
#438
#951
#276

##SOLUTION:

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [[]]:
            return 0
        
        num = 0
        
        # sliding window
        for i in range(len(grid)-3+1):
            for j in range(len(grid[0])-3+1):
                # print i,j
                # print [grid[k][j:j+3] for k in range(i,i+3)]
                if self.isMagicSquare([grid[k][j:j+3] for k in range(i, i+3)]):
                    num += 1
        return num
                
        
    def isMagicSquare(self, mat):
        # Check if nums in 1-9
        nums = set([1,2,3,4,5,6,7,8,9])
        for i in range(3):
            for j in range(3):
                if mat[i][j] in nums:
                    nums.remove(mat[i][j])
                else:
                    return False
        if len(nums) != 0:
            return False
                
        s = 0
        for i in range(3):
            s += mat[i][i]
        
        for i in range(3):
            rowS = 0
            for j in range(3):
                rowS += mat[i][j]
                
            if rowS != s:
                return False
        
        for i in range(3):
            colS = 0
            for j in range(3):
                colS += mat[i][j]
                
            if colS != s:
                return False
            
        return True
