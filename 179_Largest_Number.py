#Given a list of non negative integers, arrange them such that they form the largest number.

#For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

#Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        sorted_nums = sorted(nums, cmp = self.comparator)
        i = 0
        while i < len(sorted_nums):
            if sorted_nums[i] == 0:
                sorted_nums.pop(0)
            else:
                break
        if len(sorted_nums) == 0:
            return "0"
        
        return ''.join([str(x) for x in sorted_nums])
        
    def comparator(self, a, b):
        ab = str(a) + str(b);
        ba = str(b) + str(a);
        return cmp(int(ba), int(ab))
