"""PROBLEM:
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat
numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

"""SOLUTION: Very elegant implementation O(n)
We can use a stack to store each sub-string and the number of times the sub-string should be repeated. This can be
added to the stack every time we encounter a opening parenthesis and the sub-string can be added to the result string
every time we hit a closing parenthesis. See implementation for details.

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]]
        num_str = ""
        
        for char in s:
            if char.isdigit():
                num_str += char
            
            elif char == "[":
                stack.append(["", int(num_str)])
                num_str = ""
            
            elif char == "]":
                sub_str, times = stack.pop()
                stack[-1][0] += sub_str*times
            
            else:
                stack[-1][0] += char
            print(stack)
        
        return stack[-1][0]
        
