"""PROBLEM:
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: 
for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock 
will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of 
turns required to open the lock, or -1 if it is impossible.

"""

"""SOLUTION:
We use BFS using a deque. A queue leads to TLE. The key implementation here is to devise a way to obtain the 
next states from a given state. (That's where I got stuck! Damn!)

"""

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNeighbors(node):
            states = []
            for i, ch in enumerate(node):
                states.append(node[:i] + str((int(ch) - 1)%10) + node[i+1:])
                states.append(node[:i] + str((int(ch) + 1)%10) + node[i+1:])
            return states
        
        q = deque(['0000'])
        visited = set(deadends)
        depth = -1
        
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                q.extend(getNeighbors(node))
        return -1
        
