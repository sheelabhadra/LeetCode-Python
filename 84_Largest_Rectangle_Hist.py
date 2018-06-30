# Given n non-negative integers representing the histogram's bar height where the width 
# of each bar is 1, find the area of largest rectangle in the histogram.

## SOLUTION:

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp = [] # to hold the max rectangles
        stack = [] # to keep track of the smallest height so far

        heights.append(0)

        for i,h in enumerate(heights):
            cur_pos = i
            while stack and h < stack[-1][0]:
                cur_h, cur_pos = stack.pop()
                temp.append(cur_h*(i - cur_pos))
            stack.append([h, cur_pos])

        if temp:
            return max(temp)
        else:
            return 0
