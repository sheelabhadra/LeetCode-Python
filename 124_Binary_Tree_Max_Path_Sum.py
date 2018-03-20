#Given a binary tree, find the maximum path sum.

#For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

#For example:
#Given the below binary tree,

#       1
#      / \
#     2   3

## SOLUTION: Create a global maxval value. Find the left and right tree max path sum
# Clip them by 0 if negative. Return the path that contains the maxval.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    maxval = -2147483648
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return -2147483648
        self.MPShelper(root)
        return self.maxval
        
        
    def MPShelper(self, root):
        if root == None:
            return -2147483648
        ls = max(0, self.MPShelper(root.left))
        rs = max(0, self.MPShelper(root.right))
        self.maxval = max(self.maxval, ls+rs+root.val)
        return root.val + max(ls,rs)
        
