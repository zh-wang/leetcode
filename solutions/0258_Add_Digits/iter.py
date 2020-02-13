class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            v = 0
            while num > 0:
                v += (num % 10)
                num //= 10
            num = v
        return num
