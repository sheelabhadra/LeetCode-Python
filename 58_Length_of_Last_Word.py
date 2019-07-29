"""PROBLEM:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word 
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i -= 1
        if i == -1:
            return 0
        
        last_word_length = 0
        while i >= 0 and s[i] != " ":
            last_word_length += 1
            i -= 1

        return last_word_length
        
