# Starting with a positive integer N, we reorder the digits in any order (including the original order) 
# such that the leading digit is not zero.

# Return true if and only if we can do this in a way such that the resulting number is a power of 2.

## SOLUTION: Nice solution!! (not mine though :|)
# Since the leading digit is not zero, the reordered number shares the same number of digits with original one.
# The search base can be greatly reduced.
# Return true if Counter(N) == Counter(power of 2) and NumberOfDigits(N) == NumberOfDigits(power of 2)

from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits_of_n = len(str(N))
        counter = Counter(str(N))
        power = 1

        while True:
            digits_of_power = len(str(power))

            if digits_of_power > digits_of_n:
                break
            
            if digits_of_power == digits_of_n and Counter(str(power)) == counter:
                return True

            power = power*2

        return False
