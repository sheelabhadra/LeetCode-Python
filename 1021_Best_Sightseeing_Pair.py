"""PROBLEM:
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing
spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing
spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
"""

"""SOLUTION:
Reformulate the problem into max((A[i] + i) + (A[j] - j)). Initialize prev_max = A[0] + 0.
Update the result if prev_max + A[j] - j is max. Update prev_max if A[j] + j is greater than the prev_max.
"""

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        prev_max = A[0]
        res = 0
        for j in range(1, len(A)):
            res = max(res, prev_max + A[j] - j)
            prev_max = max(prev_max, A[j] + j)
        return res
            
