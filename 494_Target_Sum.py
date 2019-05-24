"""PROBLEM:
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""

"""SOLUTION:
Create a dictionary with the string as the key and the number of ways to get to the target sum against it. Then run
DFS adding each element in the list at each level of the tree.

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def helper(nums, cur_idx, target_sum):
            s = str(cur_idx) + "," + str(target_sum)
            if s in d:
                return d[s]

            if cur_idx == len(nums):
                if target_sum == 0:
                    return 1
                return 0

            num_ways_minus = helper(nums, cur_idx+1, target_sum + nums[cur_idx])
            num_ways_plus = helper(nums, cur_idx+1, target_sum - nums[cur_idx])

            num_ways = num_ways_minus + num_ways_plus
            d[s] = num_ways
            return num_ways
    
        d = {}
        return helper(nums, 0, S)
 
