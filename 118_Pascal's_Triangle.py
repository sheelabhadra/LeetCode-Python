"""PROBLEM:
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""

"""SOLUTION:
Using recursion. 

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        def addrow(numRows, row):
            if numRows == 1:
                return row
            
            new = [1,1]
            for n in range(len(row)-1):
                new.insert(n+1, row[n] + row[n+1])
            
            pas.append(new)
            return addrow(numRows-1, new)     
        
        pas = [[1]]
        addrow(numRows, [1])
        return pas
        
