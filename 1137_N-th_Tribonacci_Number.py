"""PROBLEM:
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0]*(n+1)
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        cache[0], cache[1], cache[2] = 0, 1, 1
        
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
            
        return cache[n]
        
