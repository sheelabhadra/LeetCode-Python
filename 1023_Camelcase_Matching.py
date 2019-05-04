"""PROBLEM:

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query.
(We may insert each character at any position, and may insert 0 characters.)
Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if 
queries[i] matches the pattern.

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
"""

"""SOLUTION:
The match process uses i for query pointer and j for pattern pointer, each iteration;

1. If current char query[i] matches pattern[j], increase pattern pointer
2. if does not match and query[i] is lowercase, keep going
3. if does not match and query[i] is captalized, we should return false

If this pattern matches, j should equal length of pattern at the end.
"""

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            res.append(self.checkMatch(query, pattern))
        return res

    def checkMatch(self, query, pattern):
        j = 0
        for i in range(len(query)):
            if j < len(pattern) and query[i] == pattern[j]:
                j += 1
            elif ord(query[i]) >= ord('A') and ord(query[i]) <= ord('Z'):
                return False
        return j == len(pattern)
            
