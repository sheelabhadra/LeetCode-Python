# Given two strings A and B of lowercase letters, return true if and only if 
# we can swap two letters in A so that the result equals B.

## SOLUTION: O(N) time, O(1) space
# Check if there are only 2 positions where the strings differ. If it is anything other than 2
# return false. Keep track of the elements that are different.
# If the difference is 0, check if there are repeated elements in the string.

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if len(A) == 0 and len(B) == 0:
            return False
        
        flag = 0
        a_elem1, b_elem1, a_elem2, b_elem2 = A[0], B[0], A[0], B[0]
        for i in range(len(A)):
            if A[i] != B[i]:
                flag += 1
                
                if flag == 1:
                    a_elem1, b_elem1 = A[i], B[i]
                
                elif flag == 2:
                    a_elem2, b_elem2 = A[i], B[i]
                
                if flag > 2:
                    return False
        
        if flag == 0:
            # count if there are 2 same characters
            return len(set(A)) != len(A)
            
        if flag != 2:
            return False
        else:
            return a_elem1 == b_elem2 and b_elem1 == a_elem2
            
