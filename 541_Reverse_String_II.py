"""PROBLEM:
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from 
the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        stack, res = [], []
        i = 0
        while i < len(s):
            while i < len(s) and not (i//k)%2:
                stack.append(s[i])
                i += 1
            while stack:
                res.append(stack.pop())
            if i == len(s):
                break
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
              
