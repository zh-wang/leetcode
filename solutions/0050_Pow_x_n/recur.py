class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        return self.recur(x, n)

    def recur(self, x, n):
        if n == 1:
            return x
        if n & 1:
            return (self.recur(x, n // 2) ** 2) * x
        else:
            return self.recur(x, n // 2) ** 2
