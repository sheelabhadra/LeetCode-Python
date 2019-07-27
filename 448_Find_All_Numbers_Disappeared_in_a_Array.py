"""SOLUTION:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0]*len(nums)
        for n in nums:
            count[n-1] += 1
        
        res = []
        print(count)
        for i,n in enumerate(count):
            if n == 0:
                res.append(i+1)
        
        return res
   
        """
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            nums[temp] = -abs(nums[temp])
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res
        """
        
