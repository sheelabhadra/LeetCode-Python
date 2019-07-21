"""PROBLEM:
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A 
repeated two times ("abcdabcd").

"""

"""SOLUTION:
Naive solution of checking if a string B is present in a string A by iteratively repeating the string A.

"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        repeat_times = (n - 1)//m + 1 # ceil operation
        
        for i in range(2):
            if B in A*(repeat_times + i):
                return repeat_times + i
        
        return -1
        
