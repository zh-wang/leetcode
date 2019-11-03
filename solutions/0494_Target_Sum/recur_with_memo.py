class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        dp = {}
        return self.recur(nums, 0, 0, S, 1, dp)

    def recur(self, nums, i, s, S, ret, dp):
        if i >= len(nums):
            return ret if s == S else 0
        if (i, s) in dp:
            return dp[(i, s)]
        cur_ret = self.recur(nums, i+1, s+nums[i], S, ret, dp) \
                + self.recur(nums, i+1, s-nums[i], S, ret, dp)
        dp[(i, s)] = cur_ret
        return cur_ret
