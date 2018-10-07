""" Given a string S, return the "reversed" string where all characters that are not a letter stay 
    in the same place, and all letters reverse their positions.
    
    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        i, j = 0, len(S)-1
        while i < j:
            while i < j and (not S[i].isalpha() or S[i].isdigit()):
                i += 1
            while j > i and (not S[j].isalpha() or S[j].isdigit()):
                j -= 1
            if i >= j:
                break
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return ''.join(S)
        
