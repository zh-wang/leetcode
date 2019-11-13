class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ret, g = m, n
        k = 0
        while g > 0:
            g = g >> 1
            k += 1
        # 1001100
        #     i
        # to check m's i-th bit will be zero or not
        # we need to find the closest value larger than m, whose i-th bit is 0
        #
        # To do this, first find the nearest 0-bit j left to i
        # then set j-th bit to 1, set all bits right to j to 0
        # if the value <= n, it means that i-th bit will be finally flip to 0
        for i in range(k):
            if (ret >> i) & 1 == 1 and self.ithBitIsZero(i, ret, k, m, n):
                ret -= (1 << i)
        return ret

    def ithBitIsZero(self, i, ret, k, m, n):
        for j in range(i+1, k):
            if (ret >> j) & 1 == 0 and (((ret >> j) + 1) << j) <= n:
                return True
        return False
