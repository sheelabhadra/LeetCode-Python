"""PROBLEM:
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their 
absolute difference is k.

"""

"""SOLUTION:
Similar to 2 sum. We need to check if (n+k) or (n-k) is in the seen set. Also we need to store the pairs to ensure
uniqueness.

"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        pairs = set()
        if k < 0:
            return 0
        
        for n in nums:
            if (n + k) in seen:
                if (n, n + k) not in pairs:   
                    pairs.add((n, n + k))
                seen.add(n)
            
            if (n - k) in seen:
                if (n - k, n) not in pairs:   
                    pairs.add((n - k, n))
                seen.add(n)
            
            if (n + k) not in seen or not (n + k) not in seen:
                if n not in seen:
                    seen.add(n)

        return len(pairs)
        
