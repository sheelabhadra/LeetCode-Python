"""PROBLEM:
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest 
distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  
(You may return the answer in any order that satisfies this condition.)

Example 1:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

"""

"""SOLUTION:
Use BFS.
"""

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[r0,c0]]
        A = [[0]*C for row in range(R)]
        A[r0][c0] = "#"
        queue = [[r0,c0]]
        
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            r, c = queue.pop(0)
            for r_step, c_step in steps:
                new_r, new_c = r + r_step, c + c_step
                if 0 <= new_r < R and 0 <= new_c < C and A[new_r][new_c] == 0:
                    A[new_r][new_c] = "#"
                    res.append([new_r,new_c])
                    queue.append([new_r, new_c])
        return res
        
