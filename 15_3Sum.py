"""PROBLEM:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

"""SOLUTION: Frequently asked in FB interviews!!!
If duplicates isn't an issue we could solve this just like 2Sum in O(n**2) time. To handle duplicates, we sort the list.
Then for each element in the list we run 2 pointer search. If adjacent elements are equal we increment/decrement. This is
the KEY step since it allows us to skip duplicates.

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Doesn't handle duplicates --> O(n2)
        # res = []
        # for i in range(len(nums)):
        #     target = -nums[i]
        #     seen = set()
        #     for j in range(i+1,len(nums)):
        #         if (target - nums[j]) in seen:
        #             res.append([nums[i], nums[j], target-nums[j]])
        #         else:
        #             seen.add(nums[j])
        # return res
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            
            # 2 pointer
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                            left += 1

                    while left < right and nums[right] == nums[right-1]:
                            right -= 1

                    left += 1; right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    right -= 1
        
        return res
