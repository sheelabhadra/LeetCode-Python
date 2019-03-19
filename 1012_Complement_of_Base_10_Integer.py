"""PROBLEM:
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 
11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.
For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.
"""

"""SOLUTION:
Convert the integer to binary format. Then find its complement and then convert it to the base-10 format.
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        b = bin(N)[2:]
        
        comp_b = [(1-int(x)) for x in b]
        comp_b = comp_b[::-1]
        
        res = 0
        for i in range(len(comp_b)):
            res += comp_b[i]*2**i
        
        return res
        
