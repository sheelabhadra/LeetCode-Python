# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

## SOLUTION: Add the areas obtained from each step in the recursion

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [[]]:
            return 0
        
        maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    maxArea = max(area, maxArea)
        
        return maxArea
                    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        
        else:
            grid[i][j] = '#'
            return 1 + self.dfs(grid, i+1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j-1)
        
