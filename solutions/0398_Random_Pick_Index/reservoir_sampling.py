import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        k = 0
        ret = 0
        for i, v in enumerate(self.nums):
            if target == v:
                k += 1
                if random.randrange(k) == 0:
                    ret = i
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
