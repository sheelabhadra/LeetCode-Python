#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

# APPROACH:
# Keep a dictionary in which we add all the numbers and their positions as we see them. If there's
# a number = target - nums[i] in seen, then return the positons of nums[i], and target - nums[i].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i
                
