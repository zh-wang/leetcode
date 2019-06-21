class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            y = 1
            temp = x
            while y * 2 <= n:
                temp = temp * temp
                y = y << 1
            ret *= temp
            n = n - y
        return ret
