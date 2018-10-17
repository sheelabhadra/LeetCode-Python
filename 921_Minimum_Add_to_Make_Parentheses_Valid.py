"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""

""" SOLUTION: Use a stack to keep track of the balanced parantheses. When the stack is empty start a counter to count 
    the number of extra parantheses that are unbalanced. The output is the sum of the length of the stack and the count.
"""

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        d = set('(')
        stack = []
        count = 0
        for e in S:
            if e in d:
                stack.append(e)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return len(stack) + count
       
