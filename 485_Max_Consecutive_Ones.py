"""PROBLEM:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
#         start, end, maxm = None, None, float('-inf')
#         flag = False
#         for i,num in enumerate(nums):
#             if num == 1:
#                 if not flag:
#                     start = i
#                 flag = True
            
#             else:
#                 if start != None:
#                     end = i-1
#                     if end - start + 1 > maxm:
#                         maxm = end - start + 1
#                 flag = False
        
#         if flag:
#             end = len(nums)-1
        
#         if start != None:
#             return max(maxm, end - start + 1)
#         else:
#             return 0
        count = 0
        maxm = 0
        for num in nums:
            if num == 1:
                count += 1
                maxm = max(maxm, count)
            else:
                count = 0
        return maxm
        
