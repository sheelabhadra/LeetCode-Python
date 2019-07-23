"""PROBLEM:
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving 
whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        res = ""
        i, j = 0, 0
        while j < len(s):
            while j < len(s) and s[j] != " ":
                j += 1
            if j == len(s):
                res += self.reverseString(s[i:j])
                break
            res += self.reverseString(s[i:j]) + " "
            j += 1
            i = j
        return res
    
    def reverseString(self, s):
        return s[::-1]
        
