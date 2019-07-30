"""PROBLEM:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would
be if it were inserted in order.

You may assume no duplicates in the array.

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
                
        if l == 0 and target <= nums[0]:
            return 0
        elif l == 0 and nums[0] <= target <= nums[r]:
            return r
        if r == len(nums)-1 and target > nums[-1]:
            return r + 1
        elif r == len(nums)-1 and nums[l] <= target <= nums[r]:
            return l + 1
        return r
        
