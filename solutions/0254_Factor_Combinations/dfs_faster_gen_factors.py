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

        primes = collections.defaultdict(int)
        m = n
        while m >= 1:
            isPrime = True
            for i in range(2, int(m ** 0.5) + 1):
                if m % i == 0:
                    primes[i] += 1
                    isPrime = False
                    m //= i
                    break
            if isPrime:
                primes[m] += 1
                break

        self.prods = []
        self.genFactors(primes, 0, 1)

        factors = sorted(self.prods)[1:-1]

        self.ret = []
        self.gen(factors, 0, n, [])
        return self.ret

    def genFactors(self, primes, depth, prod):
        if depth >= len(primes):
            self.prods += [prod]
            return
        k = list(primes.keys())[depth]
        v = primes[k]
        for cnt in range(v + 1):
            self.genFactors(primes, depth + 1, prod * (k ** cnt))

    def gen(self, factors, start, n, arr):
        if n == 1:
            self.ret += [arr[:]]
            return
        for i in range(start, len(factors)):
            if n % factors[i] == 0 and (not arr or factors[i] >= arr[-1]):
                self.gen(factors, i, n // factors[i], arr + [factors[i]])
