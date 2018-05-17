#Given a string, find the length of the longest substring without repeating characters.

#Examples:
#Given "abcabcbb", the answer is "abc", which the length is 3.

## SOLUTION: Create a dictionary and iterate through the string.
# Key of the dictionary is the character its value is the index.
# If the current char is already present and start <= d[s[i]],
# update the start position to d[s[i]] + 1.
# Else update the maxlength.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start, max_len = 0, 0
        
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                max_len = max(max_len, i-start+1)
                print max_len
            d[s[i]] = i
        
        return max_len
            
