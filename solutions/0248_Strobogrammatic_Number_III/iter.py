# --STAR-- --Link--
# https://evelynn.gitbooks.io/google-interview/strobogrammatic_number_iii.html

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, lo, hi):
        # write your code here
        self.nums = ['0', '1', '6', '8', '9']
        self.rnums = ['0', '1', '9', '8', '6']

        n_hi, _hi = 0, int(hi)
        while _hi > 0:
            _hi //= 10
            n_hi += 1

        n_lo, _lo = 0, int(lo)
        while _lo > 0:
            _lo //= 10
            n_lo += 1

        for n in range(n_lo, n_hi + 1):
            k = self.generate(n, n & 1, ['0', '1', '8'] if n & 1 == 1 else [''], int(lo), int(hi))
            if n == n_lo or n == n_hi:
                k = list(filter(lambda v: int(lo) <= int(v) <= int(hi), k))
            print(k)

    """
    @param n: max number of digits
    @param l: current number of digits
    """
    def generate(self, n, l, ret, lo, hi):
        if l >= n:
            return ret
        newRet = []
        startIndex = 0 if l < n - 2 else 1
        for s in ret:
            for i in range(startIndex, len(self.nums)):
                new_s = self.nums[i] + s + self.rnums[i]
                newRet += [ new_s ]
        return self.generate(n, l + 2, newRet, lo, hi)

Solution().findStrobogrammatic("123", "1234")
