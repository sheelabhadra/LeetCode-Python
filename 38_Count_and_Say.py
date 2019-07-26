"""PROBLEM:
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

"""

class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for _ in range(n-1):
            num = self.nextNum(num)
        return num
        
    def nextNum(self, num):
        res = ""
        count = 1
        i = 0
        while i < len(num)-1:
            if i < len(num)-1 and num[i] != num[i+1]:
                res += str(count) + num[i]
                count = 1
                i += 1
            while i < len(num)-1 and num[i] == num[i+1]:
                count += 1
                i += 1
        
        if count > 1:
            res += str(count) + num[i]
        else:
            res += "1" + num[i]
        return res
        
            
