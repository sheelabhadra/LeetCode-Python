#There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, 
#and each room may have some keys to access the next room. 

#Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
#where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

#Initially, all the rooms start locked (except for room 0). 

#You can walk back and forth between rooms freely.

#Return true if and only if you can enter every room.

#Example 1:

#Input: [[1],[2],[3],[]]
#Output: true
#Explanation:  
#We start in room 0, and pick up key 1.
#We then go to room 1, and pick up key 2.
#We then go to room 2, and pick up key 3.
#We then go to room 3.  Since we were able to go to every room, we return true.
#Example 2:

#Input: [[1,3],[3,0,1],[2],[0]]
#Output: false
#Explanation: We can't enter the room with number 2.

## SOLUTION: Treat each room as a node and apply DFS on the directed graph.

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = [0]*n
        visited[0] = 1
        
        for j in range(len(rooms[0])):
            if visited[rooms[0][j]] == 1:
                continue
            else:
                if rooms[0][j] == 0: # Check if room number = key number
                    continue
                else:
                    visited[rooms[0][j]] = 1
                    self.dfs(visited, rooms, rooms[0][j])
        
        for n in visited:
            if n != 1:
                return False
        
        return True
        
    def dfs(self, visited, rooms, j):
        for k in rooms[j]:
            if k == j: # Check if room number = key number
                continue
            else:
                if visited[k] != 1:
                    visited[k] = 1
                    self.dfs(visited, rooms, k)
 
