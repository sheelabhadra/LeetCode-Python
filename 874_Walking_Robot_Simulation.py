# A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of 
# three possible types of commands:

# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# Some of the grid squares are obstacles. 

# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

# If the robot would try to move onto them, the robot stays on the previous grid square instead 
# (but still continues following the rest of the route.)

# Return the square of the maximum Euclidean distance that the robot will be from the origin.

## SOLUTION: LeetCode's solution

class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans
        
        
  ## My Solution: Doesn't work for 8 test cases :(
  
  class Solution(object):
#     def robotSim(self, commands, obstacles):
#         """
#         :type commands: List[int]
#         :type obstacles: List[List[int]]
#         :rtype: int
#         """
#         # -1: turn 90 right
#         # -2: turn 90 left
        
#         cur_dir = 'N'
#         x, y = 0, 0
        
#         obs_set = set()
#         for obs in obstacles:
#             if obs != [0,0]:
#                 obs_set.add((obs[0], obs[1]))
        
#         max_dist = []
        
#         for c in commands:
#             if c == -1:
#                 if cur_dir == 'N':
#                     cur_dir = 'E'
#                 elif cur_dir == 'E':
#                     cur_dir = 'S'
#                 elif cur_dir == 'S':
#                     cur_dir = 'W'
#                 else:
#                     cur_dir = 'N'
            
#             elif c == -2:
#                 if cur_dir == 'N':
#                     cur_dir = 'W'
#                 elif cur_dir == 'W':
#                     cur_dir = 'S'
#                 elif cur_dir == 'S':
#                     cur_dir = 'E'
#                 else:
#                     cur_dir = 'N'
            
#             else:
#                 flag = False
#                 if cur_dir == 'N':
#                     new_y = y + c
#                     for i in range(y+1,new_y+1):
#                         if (x,i) in obs_set:
#                             y = i-1
#                             flag = True
#                             break
#                     if not flag:
#                         y = new_y
                    
#                 elif cur_dir == 'E':
#                     new_x = x + c
#                     for i in range(x+1,new_x+1):
#                         if (i,y) in obs_set:
#                             x = i-1
#                             flag = True
#                             break
#                     if not flag:
#                         x = new_x
                    
#                 elif cur_dir == 'S':
#                     new_y = y - c
#                     for i in range(y-1,new_y-1,-1):
#                         if (x,i) in obs_set:
#                             x = i+1
#                             flag = True
#                             break
#                     if not flag:
#                         y = new_y
                
#                 else:
#                     new_x = x - c
#                     for i in range(x-1,new_x-1,-1):
#                         if (i,y) in obs_set:
#                             y = i+1
#                             flag = True
#                             break
#                     if not flag:
#                         x = new_x
                
#                 max_dist.append(x**2 + y**2)

#         return max(max_dist)
                
             
