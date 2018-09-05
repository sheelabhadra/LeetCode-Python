# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if
# for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

## SOLUTION: Keep 2 flags that check if the array is increasing or decreasing. If both the
# flags are set at any time together, return false.

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """ 
        i, n = 0, len(A)
        inc, dec = 0, 0
        while i < n-1:
            if A[i] < A[i+1]:
                inc = 1
            elif A[i] > A[i+1]:
                dec = 1
            
            if inc == 1 and dec == 1:
                return False
            i += 1
        
        return True
        
