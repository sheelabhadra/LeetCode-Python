"""Problem:
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""

"""Solution: Elegant implementation: #copied
Count the degree of each-node. If the degree is (N-1), then the node is the town judge.

"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0]*(N+1)
        for i,j in trust:
            count[i] -= 1 # out-degree
            count[j] += 1 # in-degree
        
        for i in range(1,N+1):
            if count[i] == N-1:
                return i
        
        return -1
        
