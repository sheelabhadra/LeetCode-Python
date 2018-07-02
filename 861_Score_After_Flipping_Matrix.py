# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in that row or column: 
# changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as a binary number, 
# and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

## SOLUTION: Greedy solution: Toggle elements row-wise if new value is greater.
# Toggle elements column-wise if number of new number of 1s in column is greater.

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        temp = A
        
        # Row-wise
        for i in range(len(A)):
            old_val, new_val = 0, 0
            for j in range(len(A[0])):
                old_val += temp[i][j]*2**(len(A[0])-1-j)
                temp[i][j] = 1 - temp[i][j] # toggle
                new_val += temp[i][j]*2**(len(A[0])-1-j)
                
            if new_val < old_val:
                for j in range(len(A[0])):
                    A[i][j] = 1 - A[i][j] # toggle
        
        temp = A
        
        # Column-wise
        for i in range(len(A[0])):
            old_val, new_val = 0, 0
            for j in range(len(A)):
                if temp[j][i] == 1:
                    old_val += 1
                temp[j][i] = 1 - temp[j][i] # toggle
                if temp[j][i] == 1:
                    new_val += 1
            
            if new_val < old_val:
                for j in range(len(A)):
                    A[j][i] = 1 - A[j][i] # toggle
        
        score = 0
        # Find score
        for i in range(len(A)):
            cur_row = 0
            for j in range(len(A[0])):
                cur_row += A[i][j]*2**(len(A[0])-1-j)
            score += cur_row
        print(A)
        return score       
            
