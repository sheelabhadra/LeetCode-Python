"""PROBLEM:
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

"""

"""SOLUTION:
Recursive solution.

"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.addrow(rowIndex, [1])
    
    def addrow(self, rowIndex, row):
            if rowIndex == 0:
                return row
            
            new = [1,1]
            for n in range(len(row)-1):
                new.insert(n+1, row[n] + row[n+1])
            
            return self.addrow(rowIndex-1, new)
        
