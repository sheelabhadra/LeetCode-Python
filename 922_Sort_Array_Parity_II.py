"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
"""

""" SOLUTION: 2 pointer technique, T.C.: O(n)
    Initialize odd pointer = 1 and even pointer = 0
    4 cases:
      - If elements at both the odd and even indices are correct then odd += 2, even += 2
      - If elements at both the indices are incorrect, swap them and then odd += 2, even += 2
      - If element at odd index is incorrect, then even += 2
      - If element at even index is incorrect, then odd += 2
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = 0, 1
        while odd < len(A) and even < len(A):
            if A[odd]%2 == 1 and A[even]%2 == 0:
                odd += 2
                even += 2
            elif A[odd]%2 == 0 and A[even]%2 == 1:
                A[odd], A[even] = A[even], A[odd]
                odd += 2
                even += 2
            elif A[odd]%2 == 0 and A[even]%2 == 0:
                even += 2
            else:
                odd += 2
        return A
        
