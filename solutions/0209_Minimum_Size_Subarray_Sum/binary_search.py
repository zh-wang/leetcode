class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if nums[0] >= s:
            return 1
        ret = len(nums) + 1
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i]
            target = sums[i] - s # find index of lower bound of target
            if target >= 0:
                j = self.lower_bound(sums, 0, i, target)
                ret = min(ret, i - j + 1)
        return ret if ret <= len(nums) else 0

    # return index whose value is greater than target
    def lower_bound(self, arr, l, r, target):
        while l < r:
            m = (l + r) // 2
            if arr[m] > target:
                r = m
            else:
                l = m + 1
        return l

