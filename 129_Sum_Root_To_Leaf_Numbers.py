#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

#An example is the root-to-leaf path 1->2->3 which represents the number 123.

#Find the total sum of all root-to-leaf numbers.

#For example,

#    1
#   / \
#  2   3
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.

#Return the sum = 12 + 13 = 25.

## SOLUTION: Pass root.val as an argument in a helper function and add it with
# (the sum from the previous call)*10. Also pass root.left and root.right
# as the arguments.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findSum(root,0)
    
    def findSum(self, root, s):
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return s*10 + root.val
        return self.findSum(root.left, s*10 + root.val) + self.findSum(root.right, s*10 + root.val)
