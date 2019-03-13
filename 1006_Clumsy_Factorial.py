"""PROBLEM
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.
For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations 
for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied 
using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition
or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result
is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.
"""

"""SOLUTION
Using a stack we keep track of the element to be added and subtracted.
"""

class Solution:
    def clumsy(self, N: int) -> int:
        stack = []
        operations = ["*", "/", "+", "-"]
        prev, i, j = N, N-1, 0
        
        while i > 0:
            c = operations[j % 4];
            if c == "*":
                prev *= i
            elif c == "/":
                if prev < 0:
                    prev = -prev//i
                    prev = -prev
                else:
                    prev //= i
            elif c == "+":
                stack.append(prev)
                prev = i
            else:
                stack.append(prev)
                prev = -i
            i -= 1
            j += 1
        
        while stack:
            prev += stack.pop()

        return prev
