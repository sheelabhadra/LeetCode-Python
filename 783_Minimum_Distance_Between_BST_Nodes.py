"""PROBLEM:
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two
different nodes in the tree.

"""

"""SOLUTION:
Consider the min difference between the current node and its children. Also consider the min difference between the 
left/right child and floor/ceil value in the the subtree

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = float('inf')
        
        def helper(node, floor, ceil):
            if not node:
                return

            if node.left:
                self.ans = min(self.ans, node.val - node.left.val, node.left.val - floor)
            if node.right:
                self.ans = min(self.ans, node.right.val - node.val, ceil - node.right.val)

            helper(node.left, floor, node.val)
            helper(node.right, node.val, ceil)
        
        helper(root, float('-inf'), float('inf'))
        
        return self.ans
