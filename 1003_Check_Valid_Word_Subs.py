"""Problem:
We are given that the string "abc" is valid.

From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.
(X or Y may be empty.)  Then, X + "abc" + Y is also valid.

If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc". 
Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

Return true if and only if the given string S is valid.
"""

"""Solution:
Use a stack. Iterate over the string; if the element encountered is 'c', then pop the top 2 elements of the stack.
If the top 2 elements are not ['a', 'b'] then return False.

"""

class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            if c == 'c':
                if stack[-2:] != ['a','b']:
                    return False
                else:
                    stack.pop()
                    stack.pop()
            else:
                stack.append(c)
                
        return stack == []
