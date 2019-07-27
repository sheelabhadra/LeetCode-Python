"""PROBLEM:
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
 
Example 2:
Input: [1,2,3,4]
Output: 24
"""

"""
Find the 2 min and the 3 max and compare products of min1*min2*max1 and max1*max2*max3.

"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # # Sorting solution
        # nums.sort()
        # return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        
        # Linear scan solution
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        return max(min1*min2*max1, max1*max2*max3)
        
