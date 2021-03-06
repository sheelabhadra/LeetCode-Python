"""PROBLEM:
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = [0]*26
        
        for i in range(len(s)):
            counter[ord(t[i]) - ord('a')] += 1
            counter[ord(s[i]) - ord('a')] -= 1
        
        counter[ord(t[-1]) - ord('a')] += 1
        
        for i,count in enumerate(counter):
            if count == 1:
                return chr(97+i)
                
