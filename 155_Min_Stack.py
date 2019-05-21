"""SOLUTION:
Keep track of the minimum of the stack. At every push operation, add a tuple of the current element and the current
minimum to the stack.

"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack.pop()
    
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
