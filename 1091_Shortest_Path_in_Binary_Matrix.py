"""SOLUTION: Use a BFS. We also keep track of the distance of each cell from the start cell in the queue. Keeping track of the
distance is extremely important.

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        M, N = len(grid), len(grid[0])
        visited, queue = set(), [((0,0), 1)]
        
        while queue:
            cell, dist = queue.pop(0)
            visited.add(cell)
            i,j = cell[0], cell[1]
            
            # goal test
            if i == M-1 and j == N-1:
                return dist
                
            dirns = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            
            for dirn in dirns:
                n_cell = (i + dirn[0], j + dirn[1])
                if n_cell[0] < 0 or n_cell[0] >= M or n_cell[1] < 0 or n_cell[1] >= N or grid[n_cell[0]][n_cell[1]] == 1:
                    continue
                if n_cell not in visited:
                    queue.append((n_cell, dist+1))
                    visited.add(n_cell)              
        return -1
        
