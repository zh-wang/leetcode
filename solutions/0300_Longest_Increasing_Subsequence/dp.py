class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            k = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    k = max(k, dp[j] + 1)
            dp[i] = k
        return max(dp)
