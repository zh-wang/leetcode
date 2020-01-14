import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = self.q.qsize()
        for i in range(n-1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        x = self.pop()
        self.push(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
