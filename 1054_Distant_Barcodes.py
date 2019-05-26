"""PROBLEM:
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed 
an answer exists.

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

"""

"""SOLUTION:
Create a new list sorted by the frequency of occurence of each barcode. Place the barcodes with higher frequuency in the
even positions and then fill the odd positions once the even positions are filled.

"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        d = {}
        for bc in barcodes:
            if bc in d:
                d[bc] += 1
            else:
                d[bc] = 1
        
        barcodes_freq = []
        for k,v in d.items():
            barcodes_freq.append([k,v])
        
        barcodes_freq = sorted(barcodes_freq, key=lambda x: x[1], reverse=True)
        
        barcodes_by_mode = []
        for tup in barcodes_freq:
            barcodes_by_mode.extend([tup[0]]*tup[1])
        
        res = [0]*n
        i, j = 0, 0
        while i < n:
            res[i] = barcodes_by_mode[j]
            i += 2
            j += 1
        
        i = 1
        while i < n:
            res[i] = barcodes_by_mode[j]
            i += 2
            j += 1
        
        return res
        
