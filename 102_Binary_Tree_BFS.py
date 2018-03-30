#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its level order traversal as:
#[
#  [3],
#  [9,20],
#  [15,7]
#]

## SOLUTION: Use a queue to access elements. To print each level create an empty list
# 'level' every time all the nodes at a particular level are accessed.
At each level the queue will contain nodes present at that level. Go through
# each node (pop(0)) and add their children to the queue and at the same time add the 
# popped element to 'level'.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        queue = [root]
        
        while queue:
            level = []
            count = len(queue)
            for i in range(count):
                root = queue.pop(0)
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level)
        return res
            
