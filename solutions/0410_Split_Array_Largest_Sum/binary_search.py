class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Each group contains at least one value,
        # Therefore low >= max(nums)
        # This also makes implement in isOK to be easier (No need to do *** part)
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.isOK(nums, m, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def isOK(self, nums, m, target):
        num_of_groups, t = 1, 0
        for v in nums:
            if v <= target - t:
                t += v
            else:
                num_of_groups, t = num_of_groups + 1, v
                # *** check a single number is larger than target
                # if v > target:
                    # return False
        return num_of_groups <= m
