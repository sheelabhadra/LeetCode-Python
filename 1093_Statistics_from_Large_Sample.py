"""PROBLEM:
We sampled integers between 0 and 255, and stored the results in an array count:  count[k] is the number of integers we 
sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers. 
The mode is guaranteed to be unique.

"""

"""SOLUTION: copied :|
counts = [0, 1, 3, 4, 0, ...]    // The original array is [1,2,2,2,3,3,3,3]
step 0: Initial state
	l = 1, r = 3, nl = 0, nr = 0
step 1: Move right pointer
	l = 1, r = 2, nl = 0, nr = 4
step 2: Move left pointer
	l = 2, r = 2, nl = 1, nr = 4
step 3: Move left pointer
	l = 3, r = 2, nl = 4, nr = 4
step 4: End
Depends on the total number of left part and right part, we can find the median.
if ( number of left part < number of right part), then median is in the right part.
if ( number of left part > number of right part), then median is in the left part.
if ( number of left part == number of right part), it means the total numbers are even and median 
is equal to (the left-most number in the right part + the right-most number in the left part) / 2.

"""

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        l = 0
        r = 255
        nl = 0
        nr = 0
        minm = 255
        maxm = -1
        med1 = 0
        med2 = 0
        mode = 0
        mean = 0
        median = 0
        
        while l <= r:
            while count[l] == 0:
                l += 1
            while count[r] == 0:
                r -= 1
            
            if nl < nr:
                mean += count[l]*l;
                nl += count[l]
                if count[l] > count[mode]:
                    mode = l
                minm = min(minm, l)
                med1 = l
                l += 1
            
            else:
                mean += count[r]*r
                nr += count[r]
                if count[r] > count[mode]:
                    mode = r
                maxm = max(maxm, r)
                med2 = r
                r -= 1
                
        mean /= (nl+nr)

        if nl < nr:
            median = med2
        elif nl > nr:
            median = med1
        else:
            median = (med1 + med2)/2;
        
        return [float(minm), float(maxm), mean, median, float(mode)]
        
