#Given a binary tree, return all root-to-leaf paths.

#For example, given the following binary tree:

#   1
# /   \
#2     3
# \
#  5
#All root-to-leaf paths are:

#["1->2->5", "1->3"]

## SOLUTION: Pass a string and the result array in a helper function. Add the str(root.val)
# to the string. Pass root.left/root.right, string+"->", and result array recursively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        string = ""
        res = []
        self.paths(root, string, res)
        return res
        
    def paths(self, root, string, res):
        string += str(root.val)
        
        if root.left:
            self.paths(root.left, string+"->", res)
        if root.right:
            self.paths(root.right, string+"->", res)
        if not root.left and not root.right:
            res.append(string)
        
