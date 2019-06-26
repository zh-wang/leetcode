from functools import reduce
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        ret = 0
        nums = [i+1 for i in range(n)]
        total = reduce((lambda x, y: x * y), nums)
        span = n
        while k >= 0 and span > 0:
            total //= span
            i = k // total
            ret = ret * 10 + nums[i]
            del nums[i]
            k = k % total
            span -= 1
        return str(ret)
