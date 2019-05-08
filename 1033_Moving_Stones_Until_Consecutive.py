"""PROBLEM:
Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it
to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions 
x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an 
integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  
Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

"""

"""SOLUTION:
The maximum number of moves would be the total number of empty spots between the stones.

The minimum number of moves can be obtained by analyzing the following 4 cases:
1. If the number of empty spots between any one of the pairs of successive stones is 1,
e.g. [1, 3, 5], and [3, 5, 10], then only 1 move is required which fills the empty spot between the pair of stones.
2. If there are no empty spots between both the successive pair of stones, e.g. [1, 2, 3], then no move is required.
3. If there is no empty spot between any one of the pairs of successive stones, 
e.g. [2, 10, 11] or [2, 3, 10], then only 1 move is required.
4. For all the other possible configurations, at least 2 moves are required.

"""

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a, b, c])
        max_moves = (stones[1] - stones[0] - 1) + (stones[2] - stones[1] - 1) # points between the stones
        
        # add cases for min_moves
        if stones[1] - stones[0] == 2 or stones[2] - stones[1] == 2:
            # [1, 3, 5]
            min_moves = 1
        elif stones[1] - stones[0] == 1 and stones[2] - stones[1] == 1:
            # [1, 2, 3]
            min_moves = 0
        elif stones[1] - stones[0] == 1 or stones[2] - stones[1] == 1:
            # [2, 10, 11] or [2, 3, 10]
            min_moves = 1
        else:
            # all other cases
            min_moves = 2
        
        return [min_moves, max_moves]
        
