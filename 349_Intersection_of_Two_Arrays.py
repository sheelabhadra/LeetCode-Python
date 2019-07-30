"""PROBLEM:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        if not smaller:
            return []
        
        larger = set(larger)
        for num in smaller:
            if num in larger:
                if num not in res:
                    res.add(num)
        
        return list(res)
