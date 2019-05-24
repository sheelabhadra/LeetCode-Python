"""PROBLEM:
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # push all elements in stack2 to stack 1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # push all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
        
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.stack1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.stack1 and not self.stack2 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
