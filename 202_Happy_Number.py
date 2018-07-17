# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
# (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

## SOLUTION: Use a hash table to keep count of the ferquency of each new number. If freq > 1 there's a cycle.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new_n = self.getSum(n)
        
        d = {} # store the numbers in dictionary
        
        while new_n != 1:
            new_n = self.getSum(new_n)
            if new_n not in d:
                d[new_n] = 1
            else:
                return False
        
        return True
    
    def getSum(self, n):
        new_n = 0
        # get the digits of the number
        while n != 0:
            d = n%10
            new_n += d**2
            n = n/10
        
        return new_n
