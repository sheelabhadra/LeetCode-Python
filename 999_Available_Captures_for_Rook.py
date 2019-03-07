"""Problem:
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, 
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite 
colored pawn by moving to the same square it occupies.  
Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

""Solution:
Find where the rook is in the board. Then check along the same row and column in up, down, right, and left directions.
"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    start_i, start_j = i, j
                    break
        count = 0
        up = start_i - 1
        down = start_i + 1
        left = start_j - 1
        right = start_j + 1
        
        while up >= 0:
            if board[up][start_j] == "p":
                count += 1
                break
            elif board[up][start_j] == "B":
                break
            else:
                up -= 1
        
        while down < 8:
            if board[down][start_j] == "p":
                count += 1
                break
            elif board[down][start_j] == "B":
                break
            else:
                down += 1

        while left >= 0:
            if board[start_i][left] == "p":
                count += 1
                break
            elif board[start_i][left] == "B":
                break
            else:
                left -= 1
                
        while right < 8:
            if board[start_i][right] == "p":
                count += 1
                break
            elif board[start_i][right] == "B":
                break
            else:
                right += 1
        
        return count
