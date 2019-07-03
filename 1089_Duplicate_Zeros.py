"""PROBLEM:
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

"""

"""SOLUTION:
Start from the end of the array and replace items in the array according to the number of zeros. Similar a the problem in CTCI.

"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
                
