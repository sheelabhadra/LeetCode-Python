"""PROBLEM:
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2 = nums[0], float('-inf')
        maxIdx = 0
        
        for i in range(1, len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                maxIdx = i
            
            elif max2 < nums[i] <= max1:
                max2 = nums[i]
                
        return maxIdx if max1 >= 2*max2 else -1
                
