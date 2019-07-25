"""PROBLEM:
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale
of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less
than 8 surrounding cells, then use as many as you can.

"""

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        # pixels at the corners and on the edges are special
        m, n = len(M), len(M[0])
        
        res = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                count, total = 0, 0
                for r in (i-1, i, i+1):
                    for c in (j-1, j, j+1):
                        if 0 <= r < m and 0 <= c < n:
                            total += M[r][c]
                            count += 1
                res[i][j] = total//count
        return res
        
