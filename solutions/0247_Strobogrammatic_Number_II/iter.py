# --STAR-- --Link--
# https://www.lintcode.com/problem/strobogrammatic-number-ii/description

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        self.nums = ['0', '1', '6', '8', '9']
        self.rnums = ['0', '1', '9', '8', '6']
        ret = ['0', '1', '8'] if n & 1 == 1 else ['']
        return self.generate(n, ret)

    def generate(self, n, ret):
        if len(ret[0]) >= n:
            return ret
        newRet = []
        startIndex = 0 if len(ret[0]) < n - 2 else 1
        for s in ret:
            for i in range(startIndex, len(self.nums)):
                newRet += [ self.nums[i] + s + self.rnums[i] ]
        return self.generate(n, newRet)k
