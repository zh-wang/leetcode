import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [-1 << 32]
        for i in range(len(nums)):
            l, r = 0, len(dp) - 1
            if nums[i] > dp[-1]: # nums[i] is larger and all values in dp
                dp += [nums[i]] # inc dp array
            else:
                p = bisect.bisect_left(dp, nums[i])
                if dp[p-1] < nums[i] < dp[p]:
                    dp[p] = nums[i]
        return len(dp) - 1
