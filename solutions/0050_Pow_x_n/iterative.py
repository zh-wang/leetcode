class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ret = 1
        while n > 0:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1
        return ret
