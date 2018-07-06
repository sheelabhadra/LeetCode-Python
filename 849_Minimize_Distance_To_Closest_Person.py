# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to closest person.

## SOLUTION: Get the maximum contiguous sequence of 0s. If the max sequence occurs at the extremes
# then that is the minimum distance between 2 persons. Else the minimum distance would be the 
# maximum of the distance at the extremes, and the maximum distance//2 (or maximum distance//2 + 1) in between 2 1s.

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i,j = -1,0
        max_zeros = 0
        
        while j < len(seats):
            if seats[j] == 0:
                j += 1
            else:
                count = j-i-1
                max_zeros = max(max_zeros,count)
                i = j
                j += 1
        
        if j == len(seats):
            max_zeros = max(max_zeros, j-i-1)
        # print max_zeros
        # if max_zeros is at the extremes, then max_dist = max_zeros
        i, count1 = 0, 0
        while i < len(seats):
            if seats[i] == 0:
                count1 += 1
                i += 1
            else:
                break
        
        i, count2 = len(seats) - 1, 0
        
        while i > 0:
            if seats[i] == 0:
                count2 += 1
                i -= 1
            else:
                break
        # print count1, count2
        if count1 == max_zeros or count2 == max_zeros:
            return max_zeros
        
        else:
            if max_zeros%2 == 0:
                return max(count1, count2, max_zeros//2)
            else:
                return max(count1, count2, max_zeros//2 + 1)
        
