"""PROBLEM:
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

"""

"""SOLUTION:
The optimal condition is obtained when each player selects 1 i.e x = 1. We just need to check if N = 1 after
doing (N - x) multiple times. If N = 1 when Alice makes a move, then she loses which can be easily checked
since the turn number when Alice makes a move is always even.

"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        count, x = 0, 1
        while N > 1:
            N, count = N - x, count + 1
            if N == 1:
                if count%2 == 0:
                    return False
                else:
                    return True
        return False
        
