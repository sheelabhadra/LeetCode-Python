#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
#which sum to n.

#For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

## SOLUTION: Dynamic Programming

import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            minm = sys.maxsize
            j = 1
            while i - j*j >= 0:
                minm = min(minm, dp[i - j*j]+1)
                j += 1
            dp[i] = minm
        return dp[n]
        
