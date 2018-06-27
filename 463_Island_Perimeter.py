# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" 
# (water inside that isn't connected to the water around the island). One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## SOLUTION: Check along the horizontal and vertical directions of the grid. If adjacent cells are not equal
# increment the perimeter by 1. Also take care of the 1s lying along the edges of the grid.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [[]]:
            return 0
        
        peri = 0
        # Horizontal dirn
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j < len(grid[0]) - 1 and grid[i][j] != grid[i][j+1]:
                    peri += 1
                # If there's a 1 on the edges, increment the count
                if j == 0 and grid[i][j] == 1:
                    peri += 1
                if j == len(grid[0]) - 1 and grid[i][j] == 1:
                    peri += 1
        
        # Vertical dirn
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if j < len(grid) - 1 and grid[j][i] != grid[j+1][i]:
                    peri += 1
                # If there's a 1 on the edges, increment the count
                if j == 0  and grid[j][i] == 1:
                    peri += 1
                if j == len(grid) - 1 and grid[j][i] == 1:
                    peri += 1
        
        return peri
            
