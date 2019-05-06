"""PROBLEM:
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

"""

"""SOLUTION:
For each sub-tree, run DFS get the max and min values. Update a global variable res, if |A.val - B.val| > res.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        cur_max, cur_min = float('-inf'), float('inf')
        
        def dfs(root, cur_max, cur_min):
            if not root:
                return
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            self.res = max(self.res, cur_max - cur_min)
            dfs(root.left, cur_max, cur_min)
            dfs(root.right, cur_max, cur_min)
        
        dfs(root, cur_max, cur_min)
        return self.res
