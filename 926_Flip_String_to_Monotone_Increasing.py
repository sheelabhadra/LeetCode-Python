""" A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), 
  followed by some number of '1's (also possibly 0.)

  We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

  Return the minimum number of flips to make S monotone increasing.

"""

""" SOLUTION: #Copied
    Definition:
    dp1[i]: min number of flips to make s[:i+1] to mono increasing by making s[i] to 1
    dp0[i]: min number of flips to make s[:i+1] to mono increasing by making s[i] to 0
    
    Transition function:
    dp1[i] = min(dp1[i-1], dp0[i-1]) + (1 if s[i] == '0' else 0)
    dp0[i] = dp0[i-1] + (1 if s[i] == '0' else 0)
    
    Return:
    min(dp0[-1], dp1[-1])

    Since dp1[i], dp0[i] only relies on dp1[i-1] and dp0[i-1], the space complexity can be O(1)

"""

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp1 = 1 if S[0] == '0' else 0
        dp0 = 1 if S[0] == '1' else 0
        
        for i in range(1, len(S)):
            if S[i] == '0':
                dp1 = 1 + min(dp1, dp0)
            else:
                dp1 = min(dp1, dp0)
                dp0 += 1
        return min(dp1, dp0)
