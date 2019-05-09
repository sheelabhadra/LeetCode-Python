"""PROBLEM:
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in 
any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent
to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square
with the given color, and return the final grid.

"""

"""SOLUTION: Elegant method!
Create a set - seen() that contains all the visited cells and mark them as True if they satisfy the boundary conditions. \
To check if the given conditions are satisified for a cell at least one cell around the cell should have False.

"""

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        seen = set()
        self.dfs(seen, grid, r0, c0, r0, c0, color)
        return grid
    
    def dfs(self, seen, grid, i, j, r0, c0, color):
        if (i,j) in seen:
            return True
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != grid[r0][c0]:
            return False
        
        seen.add((i,j))
        
        if self.dfs(seen, grid, i+1, j, r0, c0, color) + self.dfs(seen, grid, i-1, j, r0, c0, color) + self.dfs(seen, grid, i, j+1, r0, c0, color) + self.dfs(seen, grid, i, j-1, r0, c0, color) < 4:
            grid[i][j] = color
        return True
        
