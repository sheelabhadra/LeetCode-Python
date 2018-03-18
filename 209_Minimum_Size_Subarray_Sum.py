#Given an array of n positive integers and a positive integer s, 
#find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#For example, given the array [2,3,1,2,4,3] and s = 7,
#the subarray [4,3] has the minimal length under the problem constraint.

## SOLUTION: Use 2 pointer sliding window method

import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
#         if sum(nums) < s:
#             return 0
        
#         sum_win = 0
#         win = []
        
#         for i in range(len(nums)):
#             win.append(nums[i])
#             sum_win += nums[i]
#             if sum_win >= s:
#                 break
#         min_win = len(win)
        
#         if min_win != len(nums):
#             for i in range(min_win,len(nums)):
#                 win.append(nums[i])
#                 sum_win += nums[i]
#                 sum_win_flag = sum_win
                
#                 while sum_win_flag >= s:
#                     sum_win_flag -= win[0]
#                     if len(win) < min_win:
#                         min_win = len(win)
#                     if sum_win_flag >= s:
#                         sum_win -= win[0]
#                         win.pop(0)
            
#             return min_win
        
#         else:
#             sum_win_flag = sum_win
#             while sum_win_flag >= s:
#                 sum_win_flag -= win[0]
#                 if len(win) < min_win:
#                     min_win = len(win)
#                 if sum_win_flag >= s:
#                     sum_win -= win[0]
#                     win.pop(0)
            
#             return min_win

## More Readable solution
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
