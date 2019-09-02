class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [1 for _ in range(n + 1)] # max product ending at i, maybe negative
        dp_min = [1 for _ in range(n + 1)] # min product ending at i, maybe positive
        for i in range(n):
            dp_max[i+1] = max(dp_max[i]*nums[i], dp_min[i]*nums[i], nums[i])
            dp_min[i+1] = min(dp_max[i]*nums[i], dp_min[i]*nums[i], nums[i])
        return max(dp_max[1:])
