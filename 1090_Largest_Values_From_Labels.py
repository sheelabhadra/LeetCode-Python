"""PROBLEM:
We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

"""

"""SOLUTION:
Using sorting and dictionary. Can be optimized by using a priority queue.

"""

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        value_label = []
        label_dict = {}
        for v,l in zip(values, labels):
            value_label.append((v, l))
            label_dict[l] = 0
        
        value_label = sorted(value_label)[::-1]
        
        res = 0
        i = 0
        while num_wanted > 0 and i < len(values):
            if label_dict[value_label[i][1]] < use_limit:
                res += value_label[i][0]
                label_dict[value_label[i][1]] += 1
                num_wanted -= 1
            i += 1
        return res
        
