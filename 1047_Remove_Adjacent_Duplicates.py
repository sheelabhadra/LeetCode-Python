"""PROBLEM:
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

"""

"""SOLUTION: Elegant solution: Using stack - one pass O(n) - Holy shit!!!
Key idea: the duplicates are to be removed in pairs. This makes stack the best option.

We iterate through the characters in the string. If the stack is empty, we add the current character to it.
If the character at the top of the stack and the current element are same, then pop from the stack. If the other cases
we add the current character to stack.

"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        """My Hacky solution
        if len(S) == 1:
            return S
        
        while S:
            res = ""
            i, j = 0, 1
            while j < len(S):
                if S[i] == S[j]:
                    i += 2
                    j += 2

                else:
                    res += S[i]
                    i += 1
                    j += 1
            if i == len(S) - 1:
                res += S[i]
    
            S = res
            if len(res) == 1:
                break
                
            else:
                k, flag = 1, False
                while k < len(res):
                    if res[k] == res[k-1]:
                        flag = True
                    k += 1
                if not flag:
                    break
        
        return S
        """
        
        res = []
        
        for c in S:
            if not res:
                res.append(c)
                continue
            if c == res[-1]:
                res.pop()
                continue
            res.append(c)
        
        return ''.join(res)
        
