""" Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

    Here, a circular array means the end of the array connects to the beginning of the array.  
    (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
"""

""" SOLUTION: Very elegant solution. Not mine though! #copied
    Keep track of maxSum, curMax, minSum, curMin, totalSum. If maxSum > 0, then return the max of
    maxSum and totalSum - minSum. If maxSum < 0, then return maxSum.
"""

import sys
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total, maxSum, curMax, minSum, curMin = 0, -sys.maxint + 1, 0, sys.maxint, 0
        
        for e in A:
            curMax = max(curMax + e, e)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + e, e)
            minSum = min(minSum, curMin)
            total += e
        
        if maxSum > 0:
            return max(maxSum, total-minSum)
        else:
            return maxSum
            
