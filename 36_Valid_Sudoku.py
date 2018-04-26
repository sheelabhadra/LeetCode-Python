#Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

##SOLUTION: Brute force; check all 3 cases

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Along row
        for i in range(9):
            nums = [str(x) for x in range(1,10)]
            nums = set(nums)
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in nums:
                    nums.remove(board[i][j])
                else:
                    return False
        
        # Along column
        for i in range(9):
            nums = [str(x) for x in range(1,10)]
            nums = set(nums)
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in nums:
                    nums.remove(board[j][i])
                else:
                    return False
                
        # In sub-matrix
        for k in range(3):
            for l in range(3):
                nums = [str(x) for x in range(1,10)]
                nums = set(nums)
                for i in range(3*k, 3*k + 3):
                    for j in range(3*l, 3*l + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in nums:
                            nums.remove(board[i][j])
                        else:
                            return False
        
        return True
