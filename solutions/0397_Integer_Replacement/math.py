class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 2 == 0: # half n when n is even
                n >>= 1
            # every odd integer mod 4 is either 1 or 3
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            cnt += 1
        return cnt
