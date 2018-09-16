# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, 
# then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only 
# carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?

## SOLUTION: Took help of solution for implementation details.
# Create a dict that stores the count of elements and a pointer i that points to the start of the sliding window.
# When the size of dict > 2, delete the elements pointed to by i one by one.
# Keep track of the max size of the sliding window.

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        n = len(tree)
        d = {}
        res, i = 0, 0
        for j,ele in enumerate(tree):
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1
            while len(d) > 2:
                d[tree[i]] -= 1
                if d[tree[i]] == 0:
                    del d[tree[i]]
                i += 1
            
            res = max(res, j - i + 1)
        return res
            
