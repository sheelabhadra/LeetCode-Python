# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.

## SOLUTION: Use recursion. Base case - if one of the nodes is None return the other.
# Recursive step - Add the values in the 2 nodes. Do recursion on the left and right chidren of 
# both the nodes of t1 and t2 and assign them to one of the nodes left and right child respectively


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        
        t1.val += t2.val
        
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
        
        
