"""PROBLEM:
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number 
(from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:
Input: [0,1,1]
Output: [true,false,false]
"""

"""SOLUTION: Using bit-wise left shift we can compute the new number that is obtained as we access
each element in the array in the loop.
"""

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num, res = A[0], [A[0]%5 == 0]
        for i in range(1, len(A)):
            num = num<<1
            num += A[i]
            res.append(num%5 == 0)
        return res
        
