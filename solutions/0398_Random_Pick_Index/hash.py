import random

class Solution:

    def __init__(self, nums: List[int]):
        self.freq = collections.defaultdict(list)
        for i, v in enumerate(nums):
            self.freq[v] += [i]

    def pick(self, target: int) -> int:
        return random.choice(self.freq[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
