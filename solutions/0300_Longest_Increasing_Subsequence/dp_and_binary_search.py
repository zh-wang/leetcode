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
                while l < r: # find the correct position, update dp[l]
                    m = (l + r) // 2
                    if dp[m] > nums[i]:
                        r = m
                    else:
                        l = m + 1
                if dp[l-1] < nums[i] < dp[l]:
                    dp[l] = nums[i]
        return len(dp) - 1
