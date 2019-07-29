"""SOLUTION:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency 
of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        degree = 0
        candidates = []
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        degree = max(d.values())
        candidates = [k for k, v in d.items() if v == degree]
        
        res = []
        for cand in candidates:
            res.append(self.minSubArrayLength(nums, cand))
        
        return min(res)
    
    def minSubArrayLength(self, nums, n):
        start, end = None, None
        for i in range(len(nums)):
            if nums[i] == n:
                start = i
                break
                
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == n:
                end = j
                break
               
        return end-start+1
