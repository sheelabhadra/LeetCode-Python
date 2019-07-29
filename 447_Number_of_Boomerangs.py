"""PROBLEM:
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the 
distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the 
range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

"""

"""SOLUTION:
Use a dictionary to store the occurence of each distance at each iteration. If there are points at the same distance from
the current point, then the new point will form pairs with the existing points. So we multiply the number by 2 and add
it to the number of boomerangs.

"""

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
                if dist in d:
                    count += 2*d[dist] # for 2 possibilities
                    d[dist] += 1
                else:
                    d[dist] = 1
        return count
