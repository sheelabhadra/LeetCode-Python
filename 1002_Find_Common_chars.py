"""Problem:
Given an array A of strings made only from lowercase letters, return a list of all characters that 
show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times
in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

"""Solution:
Create `n` dictionaries for all the `n` strings. Then iterate over the unique characters of any of the stings
and find the minimum number of occurrence of each character.
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        chars = []
        for string in A:
            ch = list(string)
            chars.append(ch)
        
        dicts = []
        for ch in chars:
            d = {}
            for ele in ch:
                if ele in d:
                    d[ele] += 1
                else:
                    d[ele] = 1
            dicts.append(d)
        
        res = []
        for ele in set(chars[0]):
            flag = 0
            count = dicts[0][ele]
            for d in dicts:
                if ele not in d:
                    flag = 1
                else:
                    count = min(count, d[ele])
            
            if not flag:
                while count > 0:
                    res.append(ele)
                    count -= 1
        return res
                    
                
