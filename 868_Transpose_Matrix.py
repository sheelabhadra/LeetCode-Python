# Given a matrix A, return the transpose of A.

## SOLUTION: List comprehension - Visit each column and convert the elements in them into rows.

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == [[]]:
            return [[]]
        
        trA = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
        
        return trA
