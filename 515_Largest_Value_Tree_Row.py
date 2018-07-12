# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#          1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## SOLUTION: Traverse level by level using BFS. Maintain a dictionary that keeps track of the 
# largest value in each level.

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        queue = []
        d = {} # stores the highest value at the current level
        
        prev_depth = 0
        cur_depth = 1
        
        queue.append((root,0))
        
        while queue:
            node, cur_depth = queue.pop(0)
            if cur_depth in d:
                if node.val > d[cur_depth]:
                    d[cur_depth] = node.val
            else:
                d[cur_depth] = node.val
                
            if cur_depth > prev_depth:
                prev_depth = cur_depth
            
            if node.left:
                queue.append((node.left,cur_depth+1))
                
            if node.right:
                queue.append((node.right,cur_depth+1))
            
        return [d[key] for key in d]
        
