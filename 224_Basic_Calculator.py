#Implement a basic calculator to evaluate a simple expression string.

#The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
#non-negative integers and empty spaces .

#You may assume that the given expression is always valid.

#Some examples:
#"1 + 1" = 2
#" 2-1 + 2 " = 3
#"(1+(4+5+2)-3)+(6+8)" = 23

##SOLUTION: When '+'/'-' occur update th 'res' and 'sign' accordingly. 
# Push the 'res' first followed by 'sign' into a stack when the '(' occurs. Also
# update 'res' to 0. When ')' occurs first multiply 'res' by stack.pop() ('sign')
# and then pop again and add to the 'res'.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0
        
        res, num, sign, stack = 0, 0, 1, []
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + ord(s[i]) - ord("0")
                
            elif s[i] == "+":
                res += sign*num
                sign = 1
                num = 0
                    
            elif s[i] == "-":
                res += sign*num
                sign = -1
                num = 0

            elif s[i] == "(":
                # we push the res first, then sign;
                stack.append(res)
                stack.append(sign)
                # reset the sign and res for the value in the parenthesis
                sign = 1   
                res = 0

            elif s[i] == ")":
                res += sign*num
                num = 0
                res *= stack.pop() #stack.pop() is the sign before the parenthesis
                res += stack.pop() #stack.pop() now is the result calculated before the parenthesis
        res += sign*num
                
        return res
        
