"""PROBLEM:
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

"""

"""SOLUTION:
Find the area of the triangle.

"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # check the area of the triangle using Heron's method
        def getSideLength(p1, p2):
            return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
        
        a = getSideLength(points[0], points[1])
        b = getSideLength(points[1], points[2])
        c = getSideLength(points[2], points[0])
        
        s = (a + b + c)/2
        
        return True if (s-a)*(s-b)*(s-c) else False
        
