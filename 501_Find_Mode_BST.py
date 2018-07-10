# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) 
# in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

## SOLUTION: 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.reserve = set() # Store all the nodes
        self.temp = {} # Store the candidate mode nodes (count > 1) 
        self.ans = []
        
        def getMode(root):
            if root == None:
                return
            if root.val in self.reserve:
                if root.val in self.temp:
                    self.temp[root.val] += 1
                else:
                    self.temp[root.val] = 2
            else:
                self.reserve.add(root.val)
            getMode(root.left)
            getMode(root.right)
        
        getMode(root)        
        if self.temp == {}:
            return list(self.reserve)
            
        for i in self.temp:
            if self.temp[i] == max(self.temp.values()):
                self.ans.append(i)
        return self.ans
        
        
