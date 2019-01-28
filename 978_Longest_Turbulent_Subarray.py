"""A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.
"""

"""SOLUTION: Using 2 pointer technique and a flag to find the maximum window size.
"""

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return 1
        
        i, j = 0, 1
        if A[0] < A[1]:
            flag = 0
        else:
            flag = 1
            
        curr_max = 1
        while j < len(A):
            if A[j-1] < A[j] and not flag:
                flag = 1
                curr_max = max(curr_max, j-i+1)
                
            elif A[j-1] > A[j] and flag:
                flag = 0
                curr_max = max(curr_max, j-i+1)
                
            else:
                if A[j-1] == A[j]:
                    i = j
                else:
                    i = j-1
            
            j += 1
        
        return curr_max

