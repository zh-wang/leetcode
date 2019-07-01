class Solution:
    def mySqrt(self, x: int) -> int:
        i = x
        while i * i > x:
            i = (i + x // i) // 2
        return i
