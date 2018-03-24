#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.

##SOLUTION: 2 pointer technique
# 1. Start from i = 0, j = len(height) - 1.
# 2. Find the maximum water.
# 3. Increment i if height[i] < height[j] else increment j. This is done hoping that we find a 
#    a vertical line such that a larger water area is obtained.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        max_water = 0
        while i < j:
            water = min(height[j], height[i])*(j-i)
            if water > max_water:
                max_water = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
