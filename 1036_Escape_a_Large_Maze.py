"""PROBLEM:
In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent
square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

"""

"""SOLUTION:
See explanation on Leetcode.
"""

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
    
        blocked = set(map(tuple, blocked))
        
        def bfs(blocked, source, target):
            si, sj = source
            ti, tj = target
            
            visited = set()
            level = 0
            queue = [(si, sj)]
            
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.pop(0)
                    if i == ti and j == tj:
                        return True
                    for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                            if 0<=x<10**6 and 0<=y<10**6 and (x,y) not in visited and (x,y) not in blocked:
                                visited.add((x,y))
                                queue.append((x,y))
                level += 1
                
                if level == len(blocked):
                    break
                
                if not len(queue):
                    return False
            
            return True

        return bfs(blocked, source, target) and bfs(blocked, target, source)
            
