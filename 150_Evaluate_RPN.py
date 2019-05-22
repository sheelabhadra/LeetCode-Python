"""PROBLEM:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

"""

"""SOLUTION:
Use a stack.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "*", "/"])
        
        for ch in tokens:
            if ch in ops:
                b = stack.pop()
                a = stack.pop()
                if ch == "+":
                    res = (a+b)
                elif ch == "-":
                    res = (a-b)
                elif ch == "*":
                    res = (a*b)
                else:
                    res = a/b
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                stack.append(res)
                
            else:
                stack.append(int(ch))
                
        return stack[0]
                
