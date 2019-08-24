"""PROBLEM:
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number 
is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""

"""SOLUTION: Asked in Micrsoft onsite.
Use a stack to tak care of the case when all the numbers are increasing.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for i in range(len(num)):
            while stack and k > 0:
                if num[i] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])
        
        # Takes care of increasing sequence
        while k != 0:
            stack.pop()
            k -= 1
        
        start = 0
        while start < len(stack) and stack[start] == "0":
            start += 1
        
        if start < len(stack):
            return "".join(stack[start:])
        else:
            return "0"
            
