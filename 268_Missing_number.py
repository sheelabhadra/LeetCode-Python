"""PROBLEM:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1
Input: [3,0,1]
Output: 2

Example 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""

"""SOLUTION:
Because we know that nums contains n numbers and that it is missing exactly one number on the range [0..n-1][0..n−1],
we know that n definitely replaces the missing number in nums. Therefore, if we initialize an integer to n and XOR it
with every index and value, we will be left with the missing number. Consider the following example 
(the values have been sorted for intuitive convenience, but need not be):

Index	0	1	2	3
Value	0	1	3	4
missing=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
      =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
      =0∧0∧0∧0∧2
      =2
"""

class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res += (i+1) - nums[i]
        return res
