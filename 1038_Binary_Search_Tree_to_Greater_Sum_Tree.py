"""PROBLEM:
Given the root of a binary search tree with distinct values, modify it so that every node has a new value 
equal to the sum of the values of the original tree that are greater than or equal to node.val.

"""

"""SOLUTION:


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return root
    
    def helper(self, root, s):
        if root == None:
            return 0
        
        new_s = root.val + self.helper(root.right, s)
        root.val = s + new_s
        
        new_s += self.helper(root.left, root.val)
        return new_s
        
