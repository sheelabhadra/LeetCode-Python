"""PROBLEM:
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

"""

"""SOLUTION:
Run BFS everytime 1 is encountered. For each depth we increase the depth by 1.

"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    min_dist = self.bfs(matrix, m, n, i, j)
                    res[i][j] = min_dist
        
        return res
    
    def bfs(self, matrix, m, n, i, j):
        queue = [(i,j)]
        visited = set()
        min_dist = 0
        dirn = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue:
            size = len(queue)
            min_dist += 1
            for _ in range(size):
                new_cell = queue.pop(0)

                if new_cell in visited:
                    continue
                else:
                    visited.add(new_cell)
                
                for d in dirn:
                    neigh_cell = [None, None]
                    neigh_cell[0] = new_cell[0] + d[0]
                    neigh_cell[1] = new_cell[1] + d[1]
                    if neigh_cell[0] < 0 or neigh_cell[0] >= m or neigh_cell[1] < 0 or neigh_cell[1] >= n:
                        continue
                    if not matrix[neigh_cell[0]][neigh_cell[1]]:
                        return min_dist
                    queue.append(tuple(neigh_cell))
            
