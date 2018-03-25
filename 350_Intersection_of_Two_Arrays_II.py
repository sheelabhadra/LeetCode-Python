#Given two arrays, write a function to compute their intersection.

#Example:
#Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

#Note:
#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.

## SOLUTION: Store the contents in 2 hashmaps and compare their contents.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = {}, {}
        res = []
        for n in nums1:
            if n not in d1:
                d1[n] = 1
            else:
                d1[n] += 1
        for n in nums2:
            if n not in d2:
                d2[n] = 1
            else:
                d2[n] += 1
        
        for k,v in d1.items():
            if k in d2:
                res.extend([k]*min(v,d2[k]))
        return res
                
