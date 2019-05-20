"""PROBLEM:
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 > stone2:
                stones.append(stone1 - stone2)
        
        if not len(stones):
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            return abs(stones[1] - stones[0])
            
