# --Link--
# https://www.lintcode.com/problem/flatten-2d-vector/description

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.data = vec2d
        self.i, self.j = 0, 0
        # find start i (because vector may be [])
        while self.i < len(self.data) and 0 == len(self.data[self.i]):
            self.i += 1

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            ret = self.data[self.i][self.j]
            # find next i & j
            self.j += 1
            while self.i < len(self.data) and self.j >= len(self.data[self.i]):
                self.i, self.j = self.i + 1, 0
            return ret
        else:
            return None

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.i >= len(self.data):
            return False
        if self.j >= len(self.data[self.i]):
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
