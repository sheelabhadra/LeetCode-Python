"""PROBLEM:
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all
the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all 
houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum 
radius standard of heaters.

"""

"""SOLUTION:
Sort the houses and the heaters by location. Add heaters at inf and -inf. Iterate over the houses. Find minimum distance
between a house and consecutive heaters. Check implementation.

"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        dist, ans = 0, 0
        i = 0
        
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            dist = min(house - heaters[i], heaters[i+1] - house)
            ans = max(ans, dist)
        
        return ans
            
