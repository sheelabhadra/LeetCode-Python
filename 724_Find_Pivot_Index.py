"""PROBLEM:
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the 
numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

"""

"""SOLUTION:
Set right_sum = sum(nums) and left_sum = 0. Then iterate through nums and decrement right_sum. If left_sum = right_sum then 
that is the pivot index or else increment left_sum.

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
