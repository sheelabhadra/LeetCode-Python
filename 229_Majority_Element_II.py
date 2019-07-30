"""PROBLEM:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None # since there can be a max of 2 nums > n/3
        count1, count2 = 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif candidate1 == None:
                candidate1 = num
                count1 = 1
            elif candidate2 == None:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    candidate1 = None
                if count2 == 0:
                    candidate2 = None       
#         for num in nums:
#             if count1 <= 0 and num != candidate2:
#                 candidate1 = num
#             if count2 <= 0 and num != candidate1:
#                 candidate2 = num
#             count1 += 2 if num == candidate1 else -1
#             count2 += 2 if num == candidate2 else -1
        
#             print(candidate1,":", count1, " ", candidate2,":", count2)
            
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1
        
        res = []
        if count1 > len(nums)//3:
            res.append(candidate1)
        if count2 > len(nums)//3:
            res.append(candidate2)
        
        return res
