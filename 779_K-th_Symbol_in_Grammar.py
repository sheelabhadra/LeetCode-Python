"""PROBLEM:
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence 
of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

"""

"""SOLUTION:
Recursive solution. Naive recursive solution that generates entire row hits TLE. Instead, we perform a binary
search in each recursive step. See implementation for details.

"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """My solution: TLE :(
        row = self.helper(N-1, [0])
        return row[K-1]
    
    def helper(self, N, row):
        if N == 0:
            return row
        
        new = []
        
        for n in range(len(row)):
            if row[n] == 0:
                new.extend([0,1])
            else:
                new.extend([1,0])
        return self.helper(N-1, new)
        """
        
        if N == 1:
            return 0
        if N == 2:
            return [0, 1][K-1]
        
        half = (2**(N-1))//2
        
        if K <= half:
            return int(self.kthGrammar(N-1, K))
        else:
            return int(not self.kthGrammar(N-1, K-half))
            
