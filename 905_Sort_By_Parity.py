# Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

## SOLUTION: Use 2 pointer technique. Fill even elements from the start of the array
# and odd elements from the end.

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        res = [0]*len(A)
        for ele in A:
            if ele%2:
                res[j] = ele
                j -= 1
            else:
                res[i] = ele
                i += 1
        return res
           
