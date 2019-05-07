"""PROBLEM:
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

"""

"""SOLUTION:
Sort the costs list by the difference of the first and second elements. Then use 2 pointer method.

"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda cost: cost[0] - cost[1])
        
        res = 0
        left, right = 0, len(costs)-1
        
        while left < right:
            res += costs[left][0] + costs[right][1]
            left += 1
            right -= 1
        
        return res
        
