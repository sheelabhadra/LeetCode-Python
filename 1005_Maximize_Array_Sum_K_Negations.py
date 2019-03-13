"""PROBLEM
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i],
and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.
"""

"""SOLUTION
Solve for all the cases.
"""

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        
        if A[0] >= 0:
            while K > 0:
                A[0] = -A[0]
                K -= 1
            return sum(A)
        
        i=0
        while A[i] < 0 and K > 0:
            A[i] = -A[i]
            i += 1
            K -= 1
        if K == 0 or K % 2 == 0 or A[i] == 0:
            return sum(A)
        else:
            return sum(A) - 2*min(A[i-1], A[i])
            
