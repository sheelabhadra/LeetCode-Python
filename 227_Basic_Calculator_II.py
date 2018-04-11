#Implement a basic calculator to evaluate a simple expression string.

#The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
#The integer division should truncate toward zero.

#You may assume that the given expression is always valid.

#Some examples:
#"3+2*2" = 7
#" 3/2 " = 1
#" 3+5 / 2 " = 5

## SOLUTION: Use a stack to push numbers as we encounter them. If the operation is '+' or '-' we push
# num or -num resp. to the stack and if the operation is '*' or '/', we first pop from the stack, perform
# the operation with the current number and push the result to the stack. The final output is the sum of
# of the elements in the stack.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0
        
        stack, num, sign = [], 0, "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + ord(s[i]) - ord("0")
                
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)
        
