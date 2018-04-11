#Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#compute how much water it is able to trap after raining.

#For example,
#Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

##SOLUTION: Maintain 2 lists left and right that store the maximum height of the bar till each index
# from the left side and from the right side (including the current element). After that iterate
# through the array again and update the water by adding the difference between the minimum(leff[i], right[i]) at 
# that index and the height[i].
# A more efficient solution is using 2 pointer method (left and right).

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water
    
#         Using 2 arrays:
#         n = len(height)
#         if n == 0:
#             return 0
        
#         water = 0
#         left, right = [0]*n, [0]*n
        
#         left[0] = height[0]
#         for i in range(1,n):
#             left[i] = max(left[i-1], height[i])
            
#         right[n-1] = height[n-1]
#         for i in range(n-2,-1,-1):
#             right[i] = max(right[i+1], height[i])
            
#         for i in range(n):
#             water += min(left[i], right[i]) - height[i]
            
#         return water
