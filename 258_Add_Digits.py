# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# SOLUTION: Using digital root concept to solve in O(1) time

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
#         new_n = self.newNumber(num)
        
#         while new_n/10 != 0:
#             new_n = self.newNumber(new_n)
        
#         return new_n
        
#     def newNumber(self, n):
#         new_num = 0
#         while n > 0:
#             new_num += n%10
#             n /= 10
#         return new_num
        if num == 0:
            return 0
        else:
            return num % 9 if num % 9 != 0 else 9    
        
