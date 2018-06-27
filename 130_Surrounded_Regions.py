# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
# are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border
# will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


## SOLUTION: Only check the boundaries. If there is a "O" on the boundary then run DFS and convert
# all "O"s connected to it to "Y"s. Then iterate through the board again and convert all the "O"s
# to "X"s and "Y"s to "O"s.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if j == 0 and board[i][j] == "O":
                    self.dfs(i, j, board)
                if j == len(board[0])-1 and board[i][j] == "O":
                    self.dfs(i, j, board)
                if i == 0 and board[i][j] == "O":
                    self.dfs(i, j, board)
                if i == len(board)-1 and board[i][j] == "O":
                    self.dfs(i, j, board)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"

                    
    def dfs(self, i, j, board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
            return
        
        else:
            board[i][j] = "Y"
            self.dfs(i+1, j, board)
            self.dfs(i, j+1, board)
            self.dfs(i-1, j, board)
            self.dfs(i, j-1, board)
            
