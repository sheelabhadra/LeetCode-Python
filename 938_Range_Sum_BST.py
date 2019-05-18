"""PROBLEM:
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

"""SOLUTION:
We can use the BST property to prune branches. If the value at a node is < L, we do not need to explore its left subtree
and similarly if the value at a node is > R, we do not need to explore its right subtree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def helper(root):
            if not root:
                return
            if L <= root.val <= R:
                self.s += root.val
            if root.val > L:
                helper(root.left)
            if root.val < R:
                helper(root.right)
        
        self.s = 0
        helper(root)
        return self.s
        
