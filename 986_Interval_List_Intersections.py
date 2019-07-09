"""PROBLEM:
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented 
as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

"""

"""SOLUTION:
Find max of start time stamps and min of end time stamps. If lower timestamp <= higher timestamp. Increment the index
if for the interval with lower end timestamp.

"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intervals = []
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            
            if lo <= hi:
                intervals.append([lo, hi])
                
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return intervals
        
