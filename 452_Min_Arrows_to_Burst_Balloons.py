"""PROBLEM:
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is 
the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and 
hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be
at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend 
bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. 
An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot
to burst all balloons.

"""

"""SOLUTION:
Sort the locations of the balloons by their ending point. If there is are balloons whose start positions are before the
current end location then all the balloons can be shot using a single arrow. In the other case we will need an additional
arrow and we also update the ending point.

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points = sorted(points, key=lambda x: x[1])
        
        first_end = points[0][1]
        num_arrows = 1
        for start, end in points:
            if start > first_end:
                num_arrows += 1
                first_end = end
        
        return num_arrows
        
