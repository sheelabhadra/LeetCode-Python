# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

# Since the answer may be large, return the answer modulo 10^9 + 7.

# Example 1:

# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

## SOLUTION: Very important concept.
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(A)
        left, right, s1, s2 = [0]*n, [0]*n, [], []
        res = 0
        
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append((A[i], count))
        
        for i in range(n-1,-1,-1):
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append((A[i], count))
        
        for i in range(n):
            res = (res + left[i]*right[i]*A[i])%mod
        
        return res
        
