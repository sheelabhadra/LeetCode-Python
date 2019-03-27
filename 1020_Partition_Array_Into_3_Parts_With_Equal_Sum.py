"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts 
with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == 
A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

"""

"""SOLUTION:
The sum of the elements in the array must be a mutiple of 3. Find the sum required for each partition and then find the
running sum of elements in the array. If the running sum = partition sum, then update a counter indicating the presence
of a subarray with this sum. If at the end the running sum = 0 and the number of subarrays - 3 then return true.
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A)%3:
            return False
        
        partition_sum = sum(A)/3
        
        i = 0
        running_sum, count = 0, 0
        while i < len(A):
            running_sum += A[i]
            if running_sum == partition_sum:
                running_sum = 0
                count += 1
            i += 1
        
        if running_sum == 0 and count == 3:
            return True
        else:
            return False
