"""PROBLEM:
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

1. If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
2. If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
3. Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        
        i, num = 0, 1
        res = []
        
        for j in range(len(S)):
            if S[j] == " " or j == len(S)-1:
                if j == len(S)-1:
                    word = S[i:j+1]
                else:
                    word = S[i:j]
                if S[i] in vowels:
                    word = str(word) + "ma" + "a"*num
                else:
                    word = str(word[1:]) + word[0] + "ma" + "a"*num
                res.append(word)
                i = j + 1
                num += 1
        return " ".join(res)
                
