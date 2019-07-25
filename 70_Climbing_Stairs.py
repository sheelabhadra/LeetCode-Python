"""PROBLEM:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1]*(n+1)
        if n == 1:
            return cache[n]
        
        for i in range(2,n+1):
            cache[i] = cache[i-1] + cache[i-2]
            
        return cache[n]
