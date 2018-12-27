""" In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

    Return the element repeated N times.
"""

""" SOLUTION: Create a sliding window of size 4 and check if there are any repeated elements in the window.
    
"""

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Create a window of size 4 - return the element occuring more than once
        i = 0
        win = 4
        while (i + win) <= len(A):
            temp = A[i:i+win]
            if len(temp) != len(set(temp)):
                d = {}
                for j in temp:
                    if j in d:
                        d[j] += 1
                    else:
                        d[j] = 1
                for k,v in d.items():
                    if v > 1:
                        return k
            i += 1
