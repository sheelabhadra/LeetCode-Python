"""
  Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

  After this process, we have some array B.

  Return the smallest possible difference between the maximum value of B and the minimum value of B.

"""

""" SOLUTION
    Sort array A. Adding -K or K to A[i] is equivalent to adding 0 and 2K instead.
    Set initial maxm = A[-1] and minm = A[0]
    Add 2K to every element in sorted A and compare the new maxm and minm with the old maxm and minm.
    Update the difference with the new minm.
    
"""

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        if n == 1:
            return 0
        A.sort()
        diff = A[-1] - A[0]
        
        for i in range(n-1):
            maxm = max(A[-1], A[i] + 2*K)
            minm = min(A[i+1], A[0] + 2*K)
            diff = min(diff, maxm - minm)
        
        return diff 
            
