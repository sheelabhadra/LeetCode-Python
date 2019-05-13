"""PROBLEM:
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning,
each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]

"""

"""SOLUTION:

"""

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0]*(N+K)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i+1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i-k] + curMax*k)
        return dp[N-1]
        
