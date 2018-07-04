# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.

## SOLUTION: Compare adjacnet elements and keep track of the count. Also, handle the case
# when the laast element and the penultimate element are equal.

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        large_groups = []
        i, j = 0, 1
        
        while j < len(S):
            count = 1
            
            while j < len(S) and S[i] == S[j]:
                count += 1
                j += 1
            
            if j == len(S):
                if S[j-1] == S[j-2]:
                    if count >= 3:
                        large_groups.append([i,j-1])
            
            elif j < len(S) and count >= 3:
                large_groups.append([i,j-1])
            
            i = j
            j += 1
            
        return large_groups
                
