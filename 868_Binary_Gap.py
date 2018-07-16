# Given a positive integer N, find and return the longest distance between two consecutive 1's 
# in the binary representation of N.

# If there aren't two consecutive 1's, return 0.

## SOLUTION:

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)
        
        i, j = 2, 3 # ignoring the first 2 chars - "0b"
        max_dist = 0
        cur_dist = 1
        
        while j < len(s):
            if s[j] == '1':
                max_dist = max(cur_dist, max_dist)
                cur_dist = 1
                i = j
                i += 1
                j += 1
            else:
                cur_dist += 1
                j += 1
        
        return max_dist
