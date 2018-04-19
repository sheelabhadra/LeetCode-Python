#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

#Example 1:
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#Example 2:
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

##SOLUTION: Start from count = 0. If we encounter a 0 then count -= 1,
# if we encounter a 1 then count += 1. The idea is that the count will be same
# when equal number of 0s and 1s occur continuously. We keep storing the (i+1) value against
# the count value in a dict with {0: 0} also. Update maxLen if count is
# already there in the dict.

count = 0
        maxLen = 0
        
        d = {0: 0}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in d:
                maxLen = max(maxLen, i+1 - d[count])
            else:
                d[count] = i+1
        return maxLen
