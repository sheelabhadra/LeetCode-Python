"""PROBLEM:
Implement pow(x, n), which calculates x raised to the power n (xn).

"""

"""SOLUTION:
Naive recursive solution encounters TLE. To make the solution faster, if n is even at a recursive step, then we square
the result obtained at that stage and divide n by 2.

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Tail recursive solution: TLE :(
        def helper(x, n, res):
            if n == 0:
                return res
            res = x*res
            return helper(x, abs(n)-1, res)
        
        if n < 0:
            n = abs(n)
            return 1/helper(x, n, 1)

        else:
            return helper(x, n, 1)
        """
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x, n//2)
