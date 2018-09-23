"""
  Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

  After this process, we have some array B.

  Return the smallest possible difference between the maximum value of B and the minimum value of B.
  
"""

""" SOLUTION
    Find the max and min of array A. If the difference between max and min is <= 2K, we can get a min difference
    of 0. If it is > than 2K then the min difference is abs(abs(maxA - minA) - 2K)
  
"""

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        if n == 1:
            return 0
        
        maxm = max(A)
        minm = min(A)
        
        if maxm - minm <= 2*K:
            return 0
        else:
            return abs(abs(maxm - minm) - 2*K)
            
