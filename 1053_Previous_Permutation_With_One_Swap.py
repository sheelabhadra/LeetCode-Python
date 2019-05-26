"""PROBLEM:
Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation 
that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  
If it cannot be done, then return the same array.

"""

"""SOLUTION:
Starting from the end of the array, find the index for which A[idx-1] > A[idx]. We swap the number at idx-1 with the
number on the right which is the largest among all the numbers on the right but smaller than the number at idx-1.

"""

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        i = n-1
        
        while i >= 1 and A[i] >= A[i-1]:
            i -= 1
        
        if i == 0:
            return A
        
        # find the first element after (i-1) that is < A[i-1] but the largest among the rest
        # if there is none, swap with (i)
        left, right = i-1, n-1
        while A[left] <= A[right]:
            right -= 1
        while A[right - 1] == A[right]:
            right -= 1
            
        A[left], A[right] = A[right], A[left]
        
        return A
        
