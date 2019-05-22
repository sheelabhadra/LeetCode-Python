"""PROBLEM:
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days
you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""

"""SOLUTION:
Iterate from the end of the list. Use a stack. If the current element is less than the top of the stack, add the 
element to the stack along with the number of days (=1). When an element is encountered that has a value greater
than the top of the stack, pop from the stack until a value greater than the element is obtained. Keep adding the
number of days on every pop. See the actual implementation for other minute details.

"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        T = T[::-1]
        stack = [(T[0],0)]
        res = [0]
        i = 1
    
        while T[i] >= T[i-1]:
            stack.append((T[i], 0))
            res.append(0)
            i += 1 
        
        while i < len(T):
            if T[i] < stack[-1][0]:
                stack.append((T[i], 1))
                res.append(1)
                i += 1
            else:
                days = 1
                while stack and T[i] >= stack[-1][0]:
                    days += stack[-1][1]    
                    stack.pop()     
                if not stack:
                    stack.append((T[i], 0))
                    res.append(0)
                else:
                    stack.append((T[i], days))
                    res.append(days)
                i += 1
        
        return res[::-1]
                
# More elegant solution - copied
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
