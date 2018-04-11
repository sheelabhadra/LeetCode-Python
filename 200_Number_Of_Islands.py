#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.

##SOLUTION: Traverse through the grid. If grid[i][j] == '1', run DFS from the grid cell.
# If the conditions for i and j are violated or grid[i][j] != 1 then return from the DFS.
# There are 4 possible directions in which the DFS search can be done.
# Mark the visited cell by some character other than '1'.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == [[]]:
            return 0
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': 
                    self.dfs(grid, i, j)
                    numIslands += 1
        return numIslands
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        
