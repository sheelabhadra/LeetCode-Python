#Given a binary tree, determine if it is height-balanced.

#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#### SOLUTION ####

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, node):
        if node == None:
            return 0 # Null tree

        lh = self.height(node.left)
        if lh == float('-inf'):
            return float('-inf')

        rh = self.height(node.right)
        if rh == float('-inf'):
            return float('-inf')

        if abs(lh-rh) > 1:
            return float('-inf')
        else:
            return max(lh,rh) + 1

        return 1 + max(self.height(node.left), height(node.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) != float('-inf')
        
