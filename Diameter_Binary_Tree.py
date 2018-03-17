#Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#Example:
#Given a binary tree 
#          1
#         / \
#        2   3
#       / \     
#      4   5    
#Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

#Note: The length of path between two nodes is represented by the number of edges between them.

## SOLUTION: The diameter of a tree T is the largest of the following quantities:
#1. the diameter of T’s left subtree
#2. the diameter of T’s right subtree
#3. the longest path between leaves that goes through the root of T 
# (this can be computed from the heights of the subtrees of T)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        lheight = self.find_height(root.left)
        rheight = self.find_height(root.right)
        
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), lheight+rheight)
        
    def find_height(self, root):
        if root == None:
            return 0
        return 1 + max(self.find_height(root.left), self.find_height(root.right))
        
