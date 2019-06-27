from functools import reduce
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        ret = 0
        nums = [i+1 for i in range(n)]
        total = reduce((lambda x, y: x * y), nums)
        numOfGroup = n
        while k >= 0 and numOfGroup > 0:
            total //= numOfGroup # num of slots in each group
            i = k // total # the index of group
            ret = ret * 10 + nums[i]
            del nums[i]
            k = k % total # the remaining k for next loop
            numOfGroup -= 1 # the next num of group
        return str(ret)
