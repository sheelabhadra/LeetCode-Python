#Let's call an array A a mountain if the following properties hold:

#A.length >= 3
#There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
#Given an array that is definitely a mountain, return any i such that 
#A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

#Example 1:

#Input: [0,1,0]
#Output: 1

##SOLUTION: Compare adjacent elements.

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i
        return A[-1]
