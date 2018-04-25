#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, 
#and each element in the array contain a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.


##SOLUTION: Add 1 to the last element. Start iterating in the reverse order.
# Make appropriate changes if the current element is 10 (after adding 1 to it). 

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        return digits
