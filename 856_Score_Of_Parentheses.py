# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example:
# Input: "(()(()))"
# Output: 6

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        
        for c in S:
            if c == "(":
                stack.append(-1)
                
            else:
                cur = 0
                while stack[-1] != -1:
                    cur += stack.pop()
                stack.pop()
                
                if cur == 0:
                    stack.append(1)
                else:
                    stack.append(2*cur)
        
        return sum(stack)
 
