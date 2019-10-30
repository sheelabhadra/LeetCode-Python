"""PROBLEM:
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or
already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R',
if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

"""

"""SOLUTION:
Keep track of last seen 'L' and 'R' as indices (variables L and R).

1. If you see 'R' and R > L, you have R....R, turn everything to 'R'.
2. If you see 'R' and R < L, you have L...R and you don't need to do anything.
3. If you see 'L' and L > R, you have L....L, turn everything to 'L'.
if you see 'L' and L < R, you have R....L, have to pointers from both sides, lo and hi, turn a[lo]='R' and a[hi] = 'L', 
increment lo, decrement hi, make sure you do nothing when lo=hi
4. Watch out for edge cases. Note i<=dominoes.length(), this is to deal with L.. Also note L and R are initialized to -1, 
not 0.

"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        L, R = -1, -1
        arr = list(dominoes)
        for i in range(len(dominoes)+1):
            if i == len(dominoes) or arr[i] == "R":
                if R > L:
                    while R < i:
                        arr[R] = "R"
                        R += 1
                R = i
            elif arr[i] == "L":
                if L > R or (R == -1 and L == -1):
                    while L < i:
                        L += 1
                        arr[L] = "L"
                else:
                    L = i
                    lo = R + 1
                    hi = L - 1
                    while lo < hi:
                        arr[lo] = "R"
                        arr[hi] = "L"
                        lo += 1
                        hi -= 1
        return "".join(arr)
