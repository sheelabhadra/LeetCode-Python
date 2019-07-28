"""PROBLEM;
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, 
or 0 if such a subgrid doesn't exist in the grid.

Example 1:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:
Input: grid = [[1,1,0,0]]
Output: 1

"""

"""SOLUTION:
https://leetcode.com/problems/largest-1-bordered-square/discuss/345265/c%2B%2B-beats-100-
(both-time-and-memory)-concise-with-algorithm-and-image

"""

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = [[0]*n for _ in range(m)]
        v = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    h[i][j] = 1 if j == 0 else h[i][j-1] + 1
                    v[i][j] = 1 if i == 0 else v[i-1][j] + 1
                    
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    small = min(h[i][j], v[i][j])
                    while small > count:
                        if v[i][j-small+1] >= small and h[i-small+1][j] >= small:
                            count = max(count, small)
                            break
                        small -= 1
        
        return count*count
        
