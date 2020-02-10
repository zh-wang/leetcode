# --Link--
# https://www.lintcode.com/problem/factor-combinations/description

import math
import collections

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        # get factors arr
        factors = [i for i in range(2, (n // 2) + 1) if n % i == 0]
        self.ret = []
        self.gen(factors, 0, n, [])
        return self.ret

    def gen(self, factors, start, n, arr):
        if n == 1:
            self.ret += [arr[:]]
            return
        for i in range(start, len(factors)):
            if n % factors[i] == 0 and (not arr or factors[i] >= arr[-1]):

