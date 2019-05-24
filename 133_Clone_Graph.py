"""PROBLEM:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            res = Node(node.val, [])
            visited[node.val] = res
            for n in node.neighbors:
                res.neighbors.append(dfs(n))
            return res
        
        return dfs(node)
            
