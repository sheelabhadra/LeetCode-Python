#Given an array of size n, find the majority element. The majority element is the element 
#that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.

## SOLUTION: Boyer-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    
#         d = {}
#         n = len(nums)
#         for i in range(n):
#             if nums[i] not in d:
#                 d[nums[i]] = 1
#             else:
#                 d[nums[i]] += 1
        
#         for k,v in d.items():
#             print v
#             if v > float(n)/2:
#                 return k
