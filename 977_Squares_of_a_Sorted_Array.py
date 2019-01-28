"""Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

"""SOLUTION: Asked in Google internship phone interview!! :)
Use 2 pointer technique to initialize i = 0, j = len(A)-1. In the result array start from
k = len(A)-1. If A[i]**2 <= A[j]**2, then add A[j]**2 to the result otherwise add A[i]**2.

"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0]*len(A)
        i, j, k = 0, len(A)-1, len(A)-1
        while i <= j:
            if A[i]**2 <= A[j]**2:
                res[k] = A[j]**2
                j -= 1
            else:
                res[k] = A[i]**2
                i += 1
            k -= 1
        return res
        
