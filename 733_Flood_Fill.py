"""PROBLEM:
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor,
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of
the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color 
as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

"""

"""SOLUTION:
Same logic as number of islands.

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        origColor = image[sr][sc]
        self.dfs(image, m, n, sr, sc, origColor)
        
        for row in range(m):
            for col in range(n):
                if image[row][col] == "#":
                    image[row][col] = newColor
        
        return image
    
        
    def dfs(self, image, m, n, i, j, origColor):
        if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != origColor:
            return
        image[i][j] = "#"
        
        self.dfs(image, m, n, i+1, j, origColor)
        self.dfs(image, m, n, i-1, j, origColor)
        self.dfs(image, m, n, i, j+1, origColor)
        self.dfs(image, m, n, i, j-1, origColor)
 
