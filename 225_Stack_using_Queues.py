"""PROBLEM:
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        if len(self.queue1) > 1:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
        
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
    

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1:
            return self.queue1[0]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
