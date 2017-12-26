#Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

#This is case sensitive, for example "Aa" is not considered a palindrome here.

#Note:
#Assume the length of given string will not exceed 1,010.

#Example:

#Input:
#"abccccdd"

#Output:
#7

#Explanation:
#One longest palindrome that can be built is "dccaccd", whose length is 7.

#### SOLUTION ####

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lp = 0
        
        if s == '':
            return 0
        # store the frequency of characters in a dictionary
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        max_odd = 0
        for k,v in d.items():
            # include all even frequency characters
            if v%2 == 0:
                lp += v
            # include all odd frequency characters after making them even (odd-1)
            else:
                lp += (v-1)
                if v > max_odd:
                    max_odd = v
        
        if max_odd:
            return lp+1
        else:
            return lp
  
