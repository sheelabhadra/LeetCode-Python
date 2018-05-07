#Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
#Return the maximum valued number you could get.

#Example 1:
#Input: 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.

## SOLUTION: Ignore the elements upto which the digits are decreasing. Find the maximum element
# in the remaining array. Swap it with that element (minimum index) in the 1st subarray which is less
# than the maximum element in the 2nd subarray.

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = []
        temp = num
        while num != 0:
            s.append(int(num%10))
            num /= 10
        s = s[::-1]
        
        if len(s) == 1:
            return temp
        
        start = 1
        while s[start] <= s[start-1]:
            start += 1
            if start == len(s):
                break
        
        if start == len(s):
            maxnum = 0
            for i in range(len(s)):
                maxnum += (10**i)*s[len(s)-1-i]
            return maxnum
        
        maxm, idx = 0, start
        for i in range(start, len(s)):
            if s[i] >= maxm:
                maxm = s[i]
                idx = i
        
        # Find position to swap with
        i, swapidx = 0, 0
        while i < start:
            if s[i] < maxm:
                swapidx = i
                break
            else:
                i += 1
        # Swap
        s[swapidx], s[idx] = s[idx], s[swapidx]
        
        maxnum = 0
        for i in range(len(s)):
            maxnum += (10**i)*s[len(s)-1-i]
        
        return maxnum
