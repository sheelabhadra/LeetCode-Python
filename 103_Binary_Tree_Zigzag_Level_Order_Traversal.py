#Given a binary tree, return the zigzag level order traversal of its nodes' values.
#(ie, from left to right, then right to left for the next level and alternate between).

## SOLUTION: Similar to BFS. Instead of a queue use 2 stacks. Check Tushar Roy's video.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Using 2 stacks
        res = []
        if not root:
            return res
        stack1 = [root]
        stack2 = []
        
        while stack1 or stack2:
            while stack1:
                level = []
                count = len(stack1)
                
                for i in range(count):
                    root = stack1.pop()
                    level.append(root.val)
                    if root.left:
                        stack2.append(root.left)
                    if root.right:
                        stack2.append(root.right)
            
                res.append(level)
            while stack2:
                level = []
                count = len(stack2)
                
                for i in range(count):
                    root = stack2.pop()
                    level.append(root.val)
                    if root.right:
                        stack1.append(root.right)
                    if root.left:
                        stack1.append(root.left)   
                res.append(level)
        
        return res
