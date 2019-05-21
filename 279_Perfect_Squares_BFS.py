"""PROBLEM:
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

"""SOLUTION:
Using BFS and two queues.

"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        d, queue, new_queue = 1, {n}, set()
        
        while queue:
            for node in queue:
                for sq in squares:
                    if node == sq:
                        return d
                    if node < sq:
                        break
                    new_queue.add(node-sq)
            print(new_queue)
            queue, new_queue = new_queue, set()
            d += 1
            
