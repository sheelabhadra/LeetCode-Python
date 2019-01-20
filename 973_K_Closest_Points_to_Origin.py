"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""

"""SOLUTION:

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pts_with_dist = []
        for pt in points:
            dist = (pt[0]**2 + pt[1]**2)**0.5
            pts_with_dist.append([pt, dist])
        
        pts_with_dist.sort(key = lambda x: x[1])
        
        res, i = [], 0
        while i < K:
            res.append(pts_with_dist[i][0])
            i += 1
            
        return res
