# Write an iterator that iterates through a run-length encoded sequence.

# The iterator is initialized by RLEIterator(int[] A), where A is a run-length encoding of some sequence.  
# More specifically, for all even i, A[i] tells us the number of times that the non-negative integer value A[i+1] 
# is repeated in the sequence.

# The iterator supports one function: next(int n), which exhausts the next n elements (n >= 1) and returns the last
# element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.

# For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5].  
# This is because the sequence can be read as "three eights, zero nines, two fives".

## SOLUTION: We can store an index i and quantity q which represents that q elements of A[i] 
# (repeated A[i+1] times) are exhausted.

# For example, if we have A = [1,2,3,4] (mapping to the sequence [2,4,4,4]) then i = 0, q = 0 represents that nothing
# is exhausted; i = 0, q = 1 represents that [2] is exhausted, i = 2, q = 1 will represent that we have currently
# exhausted [2, 4], and so on.

# Algorithm
# Say we want to exhaust n more elements. There are currently D = A[i] - q elements left to exhaust (of value A[i+1]).
# If n > D, then we should exhaust all of them and continue: n -= D; i += 2; q = 0.
# Otherwise, we should exhaust some of them and return the current element's value: q += D; return A[i+1].

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.i = 0
        self.q = 0
        
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1
        
