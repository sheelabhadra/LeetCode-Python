#Reverse bits of a given 32 bits unsigned integer.

#For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
#return 964176192 (represented in binary as 00111001011110000010100101000000).

#### SOLUTION ####

class Solution:
    # @param n, an integer
    # @return an integer
    
#     Initializa result to 0
#     Check the last digit of the number by shifting the number right by 1
#     If digit == 1, increment the result by 1
#     else if digit == 0, do not increment the result
#     Move the result left by 1 place and continue the iteration
    
    def reverseBits(self, n):
        if n == 0:
            return 0
        
        res = 0
        for i in range(32):
            res <<= 1
            if n & 1 == 1:
                res += 1
            n >>= 1
        
        return res
        
