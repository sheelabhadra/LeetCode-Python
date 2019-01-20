"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, 
formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
"""

"""SOLUTION: Sort the list of side lengths in descending order. The first triplet for which the condition 
A[i] < A[i+1] + A[i+2] is satisfied is the triangle with the largest perimeter. Note that checking
only this condition is sufficient as the other 2 conditions are handled automatically since we
sorted the list of side lengths.

"""
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        
        return 0
        
