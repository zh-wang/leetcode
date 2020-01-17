class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1 += [x]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2:
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
