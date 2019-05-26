"""PROBLEM:
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must 
move in order for all students to be standing in non-decreasing order of height.)

"""

"""SOLUTION:
Sort the given and list and identify the locations with incorrect heights.

"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res += 1
            
        return res
        
