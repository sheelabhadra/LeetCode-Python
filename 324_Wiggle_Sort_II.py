#Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

#Example:
#(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
#(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

## SOLUTION: Sort the array in descending order. Divide it into 2 halves. Insert the lower half in
# odd indices and the upper half in the even indices. Time: O(nlogn), Space: O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
