"""PROBLEM:
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value
equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        target_node = self.helper(root, val)
        return target_node
        
    def helper(self, node, val):
        while node:
            if node.val == val:
                return node
            elif node.left and val < node.val:
                node = node.left
            elif node.right and val > node.val:
                node = node.right
            else:
                return None
                
