import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qa = queue.Queue()
        self.qb = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.qb.qsize() == 0:
            self.qa.put(x)
        else:
            self.qb.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        cur, nex = None, None
        if self.qa.qsize() == 0:
            cur, nex = self.qb, self.qa
        else:
            cur, nex = self.qa, self.qb
        while cur.qsize() > 1:
            nex.put(cur.get())
        x = cur.get()
        return x

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
        return max(self.qa.qsize(), self.qb.qsize()) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
