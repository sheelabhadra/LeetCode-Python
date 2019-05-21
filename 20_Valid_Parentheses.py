class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = set(['(', '{', '['])
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for ch in s:
            if ch in open_paren:
                stack.append(ch)
                
            if ch in d:
                if not stack:
                    return False
                
                if d[ch] != stack.pop():
                    return False
        
        return not stack
            
