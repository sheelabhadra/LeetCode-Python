# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, 
# there are receptors on each of the remaining corners, numbered 0, 1, and 2.

# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall
# at a distance q from the 0th receptor.

# Return the number of the receptor that the ray meets first. (It is guaranteed that the ray will meet a receptor eventually.)

## SOLUTION: Absolutely brilliant!! Extend the square instead of reflecting the waves. p = 5, q = 2 means that
# the ray will reach one of the receptors after 5 square blocks horizontally and 2 square blocks vertically.
# Using this approach a pattern can be found.

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p%2 == 0 and q%2 == 0:
            p = p/2
            q = q/2
        
        if p%2 == 0:
            return 2
        elif q%2 == 0:
            return 0
        else:
            return 1
            
