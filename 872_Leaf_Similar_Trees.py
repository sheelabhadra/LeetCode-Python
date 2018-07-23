# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        tree1_leaves = []
        tree2_leaves = []
        self.getLeafVal(root1, tree1_leaves)
        self.getLeafVal(root2, tree2_leaves)
        return tree1_leaves == tree2_leaves
    
    def getLeafVal(self, root, tree_leaves):
        if root == None:
            return root
        
        if root.left == None and root.right == None:
            tree_leaves.append(root.val)
        
        else:
            self.getLeafVal(root.left, tree_leaves)
            self.getLeafVal(root.right, tree_leaves)
