#A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left,right+1):
            digits = []
            temp = num
            print(num)
            while temp != 0:
                lsd = temp%10
                flag1 = 0
                if lsd == 0:
                    print("Contains 0")
                    flag1 = 1
                    break
                digits.append(lsd)
                temp = temp//10
            
            if flag1:
                continue
                
            for d in digits:
                flag2 = 0
                if num%d != 0:
                    flag2 = 1
                    break
        
            if flag2:
                continue
            else:
                res.append(num)
        print(res)
        return res
