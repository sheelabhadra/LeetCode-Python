#Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

#Formally the function should:
#Return true if there exists i, j, k 
#such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
#Your algorithm should run in O(n) time complexity and O(1) space complexity.

#Examples:
#Given [1, 2, 3, 4, 5],
#return true.

#Given [5, 4, 3, 2, 1],
#return false.

## SOLUTION: Initialize 2 mins by sys.maxsize. If current number is less than 1st min then update 1st min.
# If current number is greater than 1st min and less than 2nd min, update 2nd min.
# If both the above have occurred and current number is greater than 2nd min, return True.

import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        firstMin, secondMin = sys.maxsize, sys.maxsize
        
        for n in nums:
            if n <= firstMin:
                firstMin = n
            elif n <= secondMin:
                secondMin = n
            else:
                return True
        return False
