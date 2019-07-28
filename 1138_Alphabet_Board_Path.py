"""PROBLEM:
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].

We may make the following moves:

'U' moves our position up one row, if the square exists;
'D' moves our position down one row, if the square exists;
'L' moves our position left one column, if the square exists;
'R' moves our position right one column, if the square exists;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
Return a sequence of moves that makes our answer equal to target in the minimum number of moves. You may return 
any path that does so.

Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

"""

"""SOLUTION: Calculate the Manhattan distance to find the shifts. Special case is "z" which is the only element in the
last row.

"""

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        start = [0, 0]
        flag_z = False
        for ch in target:                
            r = (ord(ch) - 97)//5
            c = (ord(ch) - 97)%5  
            
            # character "z" - special case
            if ch == "z":
                r -= 1
            
            # manhattan distance
            moves_r = r - start[0]
            moves_c = c - start[1]
            
            if flag_z:
                if ch == "z":
                    res.append("!")
                    continue
                if moves_r <= 0:
                    res.append("U")
                    flag_z = False
            
            if moves_r > 0:
                res.extend(["D"]*moves_r)
            elif moves_r < 0:
                res.extend(["U"]*abs(moves_r))
            
            if moves_c > 0:
                res.extend(["R"]*moves_c)
            elif moves_c < 0:
                res.extend(["L"]*abs(moves_c))
            
            if ch == "z" and moves_r >= 0:
                flag_z = True
                res.append("D")
            
            if moves_r == 0 and moves_c == 0 and ch != "z":
                res.append("!")
                continue
            
            res.append("!")
            start = [r, c]
        
        return ''.join(res)

