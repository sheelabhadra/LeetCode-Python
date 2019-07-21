"""PROBLEM:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

"""
# Tail Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.helper(root.left, 1), self.helper(root.right, 1))
    
    def helper(self, node, depth):
        if not node:
            return depth
        depth += 1
        return max(self.helper(node.left, depth), self.helper(node.right, depth))
        
