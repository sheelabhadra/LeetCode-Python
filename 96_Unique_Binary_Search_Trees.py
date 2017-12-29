#Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

#For example,
#Given n = 3, there are a total of 5 unique BST's.

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

#### SOLUTION ####

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for level in range(2,n+1):
            for root in range(1,level+1):
                dp[level] += dp[level-root]*dp[root-1]
        return dp[n]
    
#    def numTrees(self, n):
#        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
