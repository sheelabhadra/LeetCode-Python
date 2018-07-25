 # Find Minimum in Rotated Sorted Array
 
 ## SOLUTION: Using binary search
 
 class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = nums[-1]
        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                low = mid
            elif nums[mid] < target:
                high = mid
            else:
                return target
        return nums[low] if nums[low] < nums[high] else nums[high]
