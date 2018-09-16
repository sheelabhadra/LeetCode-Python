# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days
# you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].

## SOLUTION: Start from the end of the temperatures list.
# And use a stack to keep track of the next biggest element

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
