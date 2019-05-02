"""PROBLEM:
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
"""

"""SOLUTION:
Check if there are 1s on the edges. Run BFS from these cells and mark all reachable 1s.
"""

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        # checks if there are 1s in the right and left edges
        vertical_edges = [0, len(A[0])-1]
        for i in range(len(A)):
            for j in vertical_edges:
                if A[i][j] == 1:
                    self.bfs(A, i, j)
        
        # checks if there are 1s in the top and bottom edges
        horizontal_edges = [0, len(A)-1]
        for j in range(len(A[0])):
            for i in horizontal_edges:
                if A[i][j] == 1:
                    self.bfs(A, i, j)
        
        enclaves = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    enclaves += 1
        return enclaves
    
    def bfs(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
            return
        
        A[i][j] = 2
        
        self.bfs(A, i+1, j)
        self.bfs(A, i-1, j)
        self.bfs(A, i, j+1)
        self.bfs(A, i, j-1)
        
