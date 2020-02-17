class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 2 == 0:
                num //= 2
                continue
            if num % 3 == 0:
                num //= 3
                continue
            if num % 5 == 0:
                num //= 5
                continue
            return False
        return True
